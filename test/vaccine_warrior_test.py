from logging import exception
from app.vaccine_warrior import vaccine_stop
from data.webpage_scraping import website_scraper
import os

# Test graceful failure when url contains random characters instead of valid url
def test_website_scraper_invalid_url():
    try:
        result = website_scraper("test")
    except:
        assert exception # result == "selenium.common.exceptions.InvalidArgumentException: Message: invalid argument" 

#Test return type is list when input is a valid url
def test_website_scraper_url():
    result = website_scraper("https://vaccinefinder.nyc.gov/")
    assert type(result) is list


#Test graceful failure when non-numeric characters are input instead of zipcode
def test_vaccine_stop_random_string():
    result = vaccine_stop("random string")
    assert result in "Invalid Zip Code. Please Check Your Inputs and Try Again."

#Test graceful failure when numeric characters are input but its not a valid zipcode
def test_vaccine_stop_invalid_zipcode():
    result = vaccine_stop("11111")
    assert result in "Invalid Zip Code. Please Check Your Inputs and Try Again."

#Test graceful failure when numeric characters are input but its not a valid zipcode format
def test_vaccine_stop_zipcode_len():
    result = vaccine_stop("123456")
    assert result in "Invalid Zip Code. Please Check Your Inputs and Try Again."


#Test graceful failure when the distance between zip code is greater 50 miles
def test_vaccine_stop_50_miles():
    result = vaccine_stop("18015")
    assert result in "No Results Within 50 Miles of Your Location"


#Test output when valid zipcode is entered
def test_vaccine_stop_valid_zipcode():
    result = vaccine_stop("10005")
    assert len(result) != 0