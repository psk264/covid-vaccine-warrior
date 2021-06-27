import datetime
from selenium import webdriver
from selenium.webdriver.common.utils import is_url_connectable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import json
import re

def website_scraper(URL):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #https://pypi.org/project/webdriver-manager/
    # driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(__file__), "..", "chromedriver.exe"), options=options)
    
    driver.get(URL)
    wait = WebDriverWait(driver, 60)
    # element = driver.find_element_by_css_selector('#availableSitesLabel > span')
    total_count_element = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Directions")))

    

    print("Scraping data from website ", URL, ". It may take some time. Thank you for your patience")
    # print(driver.title)
## - Code provided by Prof --##
    # articles = driver.find_elements_by_tag_name("article") # or use a different selector: https://selenium-python.readthedocs.io/locating-elements.html
    
    # print(len(articles))

    # for article in articles:
    #     print(article.get_property('aria-label'))
    #     print("-------------")
    #     print(type(article)) 
    #     # # https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webelement
    #     print(article.text)
##
    temp_list = []
    facility_list = []
    articles_webelements = driver.find_elements(By.TAG_NAME,'article') 
    # print(len(articles_webelements))
    for article in articles_webelements:
        # print(article.text)
        temp_list = article.text.split('\n')
        vaxtype = ""
        single_facility_dict =  {"name_of_venue": None, "facility_type": None, "vaccines_offered": None, "availability": None, "address": None, "zip_code": None, "phone_number": None}
        if (len(temp_list) !=2  ):
            for i in range(len(temp_list)):
                if("Pfizer" in temp_list[i] or "Johnson" in temp_list[i] or "Moderna" in temp_list[i]):
                    if len(vaxtype) != 0:
                        vaxtype = vaxtype + " , " +temp_list[i]
                    else: vaxtype = temp_list[i]
                if i == 0 :
                    single_facility_dict["name_of_venue"] = temp_list[i]
                elif i == 1 :
                    single_facility_dict["facility_type"] = temp_list[i]
                elif i == 2 :
                    single_facility_dict["address"] = temp_list[i]
                    single_facility_dict["zip_code"] = temp_list[i][-5:]
                elif i == 3 and "Vaccine" not in temp_list[i] : #statement to handle a case where the phone number is missing
                    single_facility_dict["phone_number"] = temp_list[i]
                elif i==5 or i==6: 
                    if("Walk-up" in temp_list[i]):  #statement to handle a case where the availability is missing
                        single_facility_dict["availability"] = temp_list[i]
                    else:
                        single_facility_dict["availability"] = "Appointment only"
            single_facility_dict["vaccines_offered"] = vaxtype
            facility_list.append(single_facility_dict)
                    
    print("Total records found: ", len(facility_list))
    # print(facility_list[0])
    return facility_list 

def store_data_json(facility_list):
    if(len(facility_list)>0):
        dir_name = "data"
        try:
            os.mkdir("data")        
        except FileExistsError:
            print("Directory \'data\' already exists!")

        current_date = datetime.datetime.now()
        file_name = os.path.join(os.path.dirname(__file__), "..", "data", "facility_data.json")
        print(file_name)

        with open(file_name, "w") as file:
            # file.write(str(facility_list))
            json.dump(facility_list,file)
    else:
        print("Sorry, file cannot be save! No data found.")
        exit()
