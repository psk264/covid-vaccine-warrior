
from data.webpage_scraping import website_scraper, store_data_json
from dotenv import load_dotenv
import os
import mpu
from uszipcode import SearchEngine
import operator
import pandas as pd
import json, ast
from pprint import pprint
from dateutil.parser import parse as parse_datetime
import requests
from pgeocode import Nominatim as Geocoder
from operator import itemgetter
import re

load_dotenv()

URL = os.getenv("URL", default="Incorrect URL, please set env var called 'URL'")

facility_list = website_scraper(URL)
store_data_json(facility_list)

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../data/facility_data.json"
abs_file_path = os.path.join(script_dir, rel_path)

openfile = open(abs_file_path)
facility_list = json.load(openfile)


# facility_list = [{'name_of_venue': 'Bedford-Stuyvesant Restoration Corporation', 'facility_type': 'Community Health Center/Clinic', 'vaccines_offered': 'Pfizer (12+),Johnson & Johnson (18+)', 'availability': 'FIRST DOSE APPOINTMENTS AVAILABLE!', 'address': '1368 Fulton Street, Community Room, Brooklyn, 11216', 'zip_code': '11216', 'phone_number': '(877) 829-4692'}, 
# {'name_of_venue': 'BMS Family Health Center at St. Paul Community Baptist Church', 'facility_type': 'Community Health Center/Clinic', 'vaccines_offered': 'Pfizer (12+)', 'availability': 'FIRST DOSE APPOINTMENTS AVAILABLE!', 'address': '859 Hendrix Street, Brooklyn, 11207', 'zip_code': '11207', 'phone_number': '(877) 829-4692'}, 
# {'name_of_venue': 'Bronx Co-Op City Dreiser Community Center', 'facility_type': 'Community Health Center/Clinic', 'vaccines_offered': 'Johnson & Johnson (18+)', 'availability': 'FIRST DOSE APPOINTMENTS AVAILABLE!', 'address': '177 Dreiser Loop, Bronx, 10475', 'zip_code': '10475', 'phone_number': '(877) 829-4692'}, 
# {'name_of_venue': 'Bronx Zoo Vaccination Site', 'facility_type': 'Community Health Center/Clinic', 'vaccines_offered': 'Pfizer (12+)', 'availability': 'Walk-up vaccinations available to all eligible New Yorkers', 'address': '2300 Southern Boulevard, Bronx, 10460', 'zip_code': '10460', 'phone_number': '(877) 829-4692'}, 
# {'name_of_venue': 'Christian Cultural Center', 'facility_type': 'Community Health Center/Clinic', 'vaccines_offered': 'Pfizer (12+)', 'availability': 'FIRST DOSE APPOINTMENTS AVAILABLE!', 'address': '12020 Flatlands Avenue, Brooklyn, 11207', 'zip_code': '11207', 'phone_number': '(877) 829-4692'}, 
# {'name_of_venue': 'Church of God East New York', 'facility_type': 'Community Health Center/Clinic', 'vaccines_offered': 'Pfizer (12+)', 'availability': 'Schedule appointment', 'address': '905 Sutter Avenue, Brooklyn, 11207', 'zip_code': '11207', 'phone_number': '(877) 829-4692'}, 
# {'name_of_venue': 'Church of the Holy Apostles', 'facility_type': 'Community Health Center/Clinic', 'vaccines_offered': 'Pfizer (12+)', 'availability': 'FIRST DOSE APPOINTMENTS AVAILABLE!', 'address': '296 9th Avenue, Manhattan, 10001', 'zip_code': '10001', 'phone_number': '(877) 829-4692'}, 
# {'name_of_venue': 'Coney Island YMCA', 'facility_type': 'Community Health Center/Clinic', 'vaccines_offered': 'Moderna (18+)', 'availability': 'Walk-up vaccinations available to all eligible New Yorkers', 'address': '2980 West 29th Street, Brooklyn, 11224', 'zip_code': '11224', 'phone_number': '(877) 829-4692'}
# ]


def vaccine_stop(zipcode):
    
    user_zip = int(zipcode)

    search = SearchEngine(simple_zipcode=True)

    zip1 = search.by_zipcode(user_zip)
    lat1 =zip1.lat
    long1 =zip1.lng

    if lat1 is None:
        print("Invalid Zip Code. Please Check Your Inputs and Try Again.")
        exit()
    else:
        distance_add = []
        for n in facility_list:
            zip2 =search.by_zipcode(n["zip_code"])
            lat2 =zip2.lat
            long2 =zip2.lng

            if lat2 is None: # some zipcode returns Null lat and long
                continue

            distance = float(mpu.haversine_distance((lat1,long1),(lat2,long2)))
            distance_add.append({
                "name_of_venue": n["name_of_venue"],
                "facility_type": n["facility_type"],
                "vaccines_offered": n["vaccines_offered"],
                "availability": n["availability"],
                "address": n["address"],
                "zip_code": n["zip_code"],
                "phone_number": n["phone_number"],
                "distance": float("{0:.2f}".format(distance))
        })

        
        facility_list_sorted = sorted(distance_add, key=itemgetter('distance')) 
        facility_list_final = facility_list_sorted[0:10]
        result="\n\n\n"
        for f in facility_list_final:
            if f["distance"] > 50:
                print("No Results Within 50 Miles of Your Location")
                exit()
            else:
                result = result + f["name_of_venue"] + "\n" + f["facility_type"] + "\n" + f["address"] + "\n" + "Distance: " + str(f["distance"]) + " Miles" + "\n" + "Vaccine Type: " + f["vaccines_offered"] + "\n" + f["availability"] + "\n" + "Phone: " + str(f["phone_number"]) + "\n\n\n"
        return result


user_zip = input("Enter the zip code: ")

result=vaccine_stop(user_zip)
print(result)

