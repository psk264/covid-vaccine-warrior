#from data.webpage_scraping import website_scraper
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL", default="Incorrect URL, please set env var called 'URL'")

#website_scraper(URL)

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "../data/facility_data.json"
abs_file_path = os.path.join(script_dir, rel_path)

openfile = open(abs_file_path)
import json
facility_list = json.load(openfile)



import json
from pprint import pprint
from dateutil.parser import parse as parse_datetime
import mpu

import requests
from dotenv import load_dotenv
from pgeocode import Nominatim as Geocoder
#from pandas import isnull
from uszipcode import SearchEngine
#from app import APP_ENV
from operator import itemgetter
#from random import shuffle

def vaccine_stop(zipcode):
    
    user_zip = int(zipcode)

    search = SearchEngine(simple_zipcode=True)

    zip1 = search.by_zipcode(user_zip)
    lat1 =zip1.lat
    long1 =zip1.lng

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
                "distance": float("{0:.1f}".format(distance))
        })

        
    facility_list_sorted = sorted(distance_add, key=itemgetter('distance')) 
    facility_list_final = facility_list_sorted[0:10]
    result="\n\n\n"
    for f in facility_list_final:
        result = result + f["name_of_venue"] + "\n" + f["facility_type"] + "\n" + f["address"] + "\n" + "Distance: " + str(f["distance"]) + " Miles" + "\n" + "Vaccine Type: " + f["vaccines_offered"] + "\n" + f["availability"] + "\n" + "Phone: " + str(f["phone_number"]) + "\n\n\n"

    return(result)