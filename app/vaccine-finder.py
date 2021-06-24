from data.webpage_scraping import website_scraper
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL", default="Incorrect URL, please set env var called 'URL'")

website_scraper(URL)