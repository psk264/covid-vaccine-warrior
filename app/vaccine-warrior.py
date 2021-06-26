from data.webpage_scraping import website_scraper, store_data_json
from dotenv import load_dotenv
import os
import mpu
from uszipcode import SearchEngine
import operator
import pandas as pd
import json, ast

load_dotenv()

URL = os.getenv("URL", default="Incorrect URL, please set env var called 'URL'")

facility_list = website_scraper(URL)
store_data_json(facility_list)

<<<<<<< Updated upstream:app/vaccine-warrior.py
# distance_list = []

# user_zip = input("Enter the zip code: ")

# #Reference: https://stackoverflow.com/questions/52292765/how-to-calculate-distance-between-two-zips
# search = SearchEngine(simple_zipcode=True)

# zip1 = search.by_zipcode(user_zip)
# lat1 =zip1.lat
# long1 =zip1.lng

# distance_add = []
# for n in facility_list:
#     zip2 =search.by_zipcode(n["zip_code"])
#     lat2 =zip2.lat
#     long2 =zip2.lng
#     distance = float(mpu.haversine_distance((lat1,long1),(lat2,long2)))
#     distance_add.append({
#             "name_of_venue": n["name_of_venue"],
#             "facility_type": n["facility_type"],
#             "vaccines_offered": n["vaccines_offered"],
#             "availability": n["availability"],
#             "zip_code": n["zip_code"],
#             "phone_number": n["phone_number"],
#             "distance": distance
#     })
# facility_list_sorted = sorted(distance_add, key=operator.itemgetter('distance')) 
# facility_list_final = facility_list_sorted[0:25]

# print(len(facility_list_final))  # 472




=======
user_zip = input("PLEASE INPUT A ZIP CODE (e.g. 10005): ")

#Reference: https://stackoverflow.com/questions/52292765/how-to-calculate-distance-between-two-zips
search = SearchEngine(simple_zipcode=True)

zip1 = search.by_zipcode(user_zip)
lat1 =zip1.lat
long1 =zip1.lng

convert_factor = 0.621371
distance_add = []
for n in facility_list:
    zip2 =search.by_zipcode(n["zip_code"])
    lat2 =zip2.lat
    long2 =zip2.lng
    distance = float(mpu.haversine_distance((lat1,long1),(lat2,long2)))
    distance_add.append({
            "name_of_venue": n["name_of_venue"],
            "facility_type": n["facility_type"],
            "vaccines_offered": n["vaccines_offered"],
            "availability": n["availability"],
            "address": n["address"],
            "zip_code": n["zip_code"],
            "phone_number": n["phone_number"],
            "distance": float("{0:.1f}".format(distance * convert_factor))
    })

      
facility_list_sorted = sorted(distance_add, key=itemgetter('distance')) 
facility_list_final = facility_list_sorted[0:25]

for f in facility_list_final:
    print(f["name_of_venue"] + "\n" + f["facility_type"] + "\n" + f["address"] + "\n" + "Distance: " + str(f["distance"]) + " Miles" + "\n" + 
    "Vaccine Type: " + f["vaccines_offered"] + "\n" + f["availability"] + "\n" + f["phone_number"] + "\n")
>>>>>>> Stashed changes:app/vaccine_warrior.py

