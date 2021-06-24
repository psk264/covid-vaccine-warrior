# app/daily_briefing.py

import os
from dotenv import load_dotenv
from datetime import date

from app import APP_ENV
from app.weather_service import get_hourly_forecasts, set_geography
from app.email_service import send_email

load_dotenv()

USER_NAME = os.getenv("USER_NAME", default="Player 1")


if __name__ == "__main__":

    print(f"RUNNING THE DAILY BRIEFING APP IN {APP_ENV.upper()} MODE...")

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

    todays_date = date.today().strftime('%A, %B %d, %Y')

    html = ""
    html += f"<h3>Good Morning, {USER_NAME}!</h3>"

    html += "<h4>Today's Date</h4>"
    html += f"<p>{todays_date}</p>"

    html += f"<h4>Weather Forecast for {result['city_name']}</h4>"
    html += "<ul>"
    for forecast in result["hourly_forecasts"]:
        html += f"<li>{forecast['timestamp']} | {forecast['temp']} | {forecast['conditions'].upper()}</li>"
    html += "</ul>"

    send_email(subject="[Daily Briefing] My Morning Report", html=html)
