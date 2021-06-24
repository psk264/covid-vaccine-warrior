# app/weather_service.py

import os
import json
from pprint import pprint
from dateutil.parser import parse as parse_datetime

import requests
from dotenv import load_dotenv
from pgeocode import Nominatim as Geocoder
from pandas import isnull

from app import APP_ENV

load_dotenv()

COUNTRY_CODE = os.getenv("COUNTRY_CODE", default="US")
ZIP_CODE = os.getenv("ZIP_CODE", default="20057")

DEGREE_SIGN = u"\N{DEGREE SIGN}"

def set_geography():
    if APP_ENV == "development":
        user_country = input("PLEASE INPUT A COUNTRY CODE (e.g. 'US'): ")
        user_zip = input("PLEASE INPUT A ZIP CODE (e.g. 20057): ")
    else:
        user_country = COUNTRY_CODE
        user_zip = ZIP_CODE
    return user_country, user_zip

def get_hourly_forecasts(country_code, zip_code):
    """
    Fetches hourly forecast information from the Weather.gov API, for a given country and zip code.

    Params:
        country_code (str) the requested country, like "US"
        zip_code (str) the requested postal code, like "20057"

    Example:
        result = get_hourly_forecasts(country_code="US", zip_code="20057")

    Returns the forecast info "hourly_forecasts" along with more information about the requested geography ("city_name").
    """
    geocoder = Geocoder(country_code)
    geo = geocoder.query_postal_code(zip_code)
    # using a null-checking method from pandas because geo is a pandas Series:
    if isnull(geo.latitude) or isnull(geo.longitude) or isnull(geo.place_name) or isnull(geo.state_code):
        return None

    # unfortunately the weather.gov api makes us do two requests or use a more sophisticated caching strategy (see api docs)
    request_url = f"https://api.weather.gov/points/{geo.latitude},{geo.longitude}"
    response = requests.get(request_url)
    if response.status_code != 200:
        return None
    parsed_response = json.loads(response.text)

    forecast_url = parsed_response["properties"]["forecastHourly"]
    forecast_response = requests.get(forecast_url)
    if forecast_response.status_code != 200:
        return None
    parsed_forecast_response = json.loads(forecast_response.text)

    # consider returning the raw geo and parsed_forecast_response objects,
    # ... and using a different method to parse them further!
    # ... but we're doing that here for now as well:
    city_name = f"{geo.place_name}, {geo.state_code}" #> Washington, DC
    hourly_forecasts = []
    for period in parsed_forecast_response["properties"]["periods"][0:24]:
        hourly_forecasts.append({
            "timestamp": format_hour(period["startTime"]),
            "temp": format_temp(period["temperature"], period["temperatureUnit"]),
            "conditions": period["shortForecast"],
            "image_url": period["icon"]
    })
    return {"city_name": city_name, "hourly_forecasts": hourly_forecasts}

def vaccine_site():
    return "testing vaccine sites"

def format_temp(temp, temp_unit="F"):
    """
    Displays a temperature to the nearest whole degree, with its temp unit a degrees symbol

    Params :
        temp (float or int) temperature
        temp_unit (str) "F" or "C"
    """
    return f"{round(temp)} {DEGREE_SIGN}{temp_unit}"

def format_hour(dt_str):
    """
    Displays a datetime-looking string as the human friendly hour like "4pm" or "16:00"

    Params : dt_str (str) a datetime like "2021-03-29T21:00:00-04:00"

    See: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/modules/datetime.md
    """
    dt = parse_datetime(dt_str)
    #return dt.strftime("%I %p") #> "01 PM"
    return dt.strftime("%H:%M") #> "13:00"


if __name__ == "__main__":

    print(f"RUNNING THE WEATHER SERVICE IN {APP_ENV.upper()} MODE...")

    # CAPTURE INPUTS

    user_country, user_zip = set_geography()
    print("COUNTRY:", user_country)
    print("ZIP CODE:", user_zip)

    # FETCH DATA

    result = get_hourly_forecasts(country_code=user_country, zip_code=user_zip)
    if not result:
        print("INVALID GEOGRAPHY. PLEASE CHECK YOUR INPUTS AND TRY AGAIN!")
        exit()

    # DISPLAY OUTPUTS

    print("-----------------")
    print(f"TODAY'S WEATHER FORECAST FOR {result['city_name'].upper()}...")
    print("-----------------")

    for forecast in result["hourly_forecasts"]:
        print(forecast["timestamp"], "|", forecast["temp"], "|", forecast["conditions"])
