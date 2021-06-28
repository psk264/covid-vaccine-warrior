
from logging import exception
import re
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
from pgeocode import Nominatim as Geocoder
from operator import itemgetter


load_dotenv()

URL = os.getenv("URL", default="Incorrect URL, please set env var called 'URL' with a valid url")
try:
    facility_list = website_scraper(URL)
    store_data_json(facility_list)
except:
    print("Incorrect URL, please set env var called 'URL' with a valid url")
    exit()    

## historically, vaccine stops were imported locally from facility_data.json
#script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
#rel_path = "../data/facility_data.json"
#abs_file_path = os.path.join(script_dir, rel_path)

# openfile = open(abs_file_path)
# facility_list = json.load(openfile)


def vaccine_stop(zipcode):
    result="\n\n\n"
    try:
        user_zip = int(zipcode)
    except ValueError:
        result = "Your Input " + str(zipcode) + " is not a Valid Zip Code. Please Check Your Inputs and Try Again."
        print(result)
        return result

    
    search = SearchEngine(simple_zipcode=True)

    zip1 = search.by_zipcode(user_zip)
    lat1 =zip1.lat
    long1 =zip1.lng

    if lat1 is None:
        result = "Your Input " + str(user_zip) + " is not a Valid Zip Code. Please Check Your Inputs and Try Again."
        print(result)
        return result
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
        
        for f in facility_list_final:
            if f["distance"] > 50:
                result = "No Results Within 50 Miles of Your Input Zip Code " + str(user_zip) + ". Please Enter a Valid NYC Zip Code."
                break
            else:
                result = result + f["name_of_venue"] + "\n" + f["facility_type"] + "\n" + f["address"] + "\n" + "Distance: " + str(f["distance"]) + " Miles" + "\n" + "Vaccine Type: " + f["vaccines_offered"] + "\n" + f["availability"] + "\n" + "Phone: " + str(f["phone_number"]) + "\n\n\n"
        return result

#This statement allows us to run the user input code conditionally i.e. 
# .. if the app is running from command line then run these statements to ask user input
# .. otherwise if running through pytest then skip the user input
if __name__ == '__main__':
    user_zip = input("Enter the zip code: ")
    result= vaccine_stop(user_zip)
    print(result)

