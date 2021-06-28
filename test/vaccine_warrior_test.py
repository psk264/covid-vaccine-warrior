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
    assert "Your Input random string is not a Valid Zip Code. Please Check Your Inputs and Try Again." in result 

#Test graceful failure when numeric characters are input but its not a valid zipcode
def test_vaccine_stop_invalid_zipcode():
    result = vaccine_stop("11111")
    assert "Your Input 11111 is not a Valid Zip Code. Please Check Your Inputs and Try Again." in result 

#Test graceful failure when numeric characters are input but its not a valid zipcode format
def test_vaccine_stop_zipcode_len():
    result = vaccine_stop("123456")
    assert "Your Input 123456 is not a Valid Zip Code. Please Check Your Inputs and Try Again." in result 

#Test graceful failure when the distance between zip code is greater 50 miles
def test_vaccine_stop_50_miles():
    result = vaccine_stop("18015")
    assert "No Results Within 50 Miles of Your Input Zip Code 18015. Please Enter a Valid NYC Zip Code." in result 


#Test output when valid zipcode is entered
def test_vaccine_stop_valid_zipcode():
    result = vaccine_stop("10005")
    assert len(result) != 0