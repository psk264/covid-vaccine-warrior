from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

def website_scraper(URL):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #https://pypi.org/project/webdriver-manager/
    # driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(__file__), "..", "chromedriver.exe"), options=options)
    
    driver.get(URL)
    

    print(type(driver))
    print(driver.title)
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
    print(len(articles_webelements))
    for article in articles_webelements:
        # print(article.text)
        temp_list = article.text.split('\n')
        single_facility_dict =  {"name_of_venue": None, "facility_type": None, "vaccines_offered": None, "availability": None, "address": None, "zip_code": None, "phone_number": None}
        if (len(temp_list) >= 9 ):
            for i in range(len(temp_list)):
                if i == 0 :
                    single_facility_dict["name_of_venue"] = temp_list[i]
                elif i == 1 :
                    single_facility_dict["facility_type"] = temp_list[i]
                elif i == 2 :
                    single_facility_dict["address"] = temp_list[i]
                    single_facility_dict["zip_code"] = temp_list[i].split(' ')[-5:0]
                elif i == 3 :
                    single_facility_dict["phone_number"] = temp_list[i]
                elif i == 5 and len(temp_list) == 10 :  #statement to handle multiple vaccine type
                    single_facility_dict["vaccines_offered"] = temp_list[i] + "," + temp_list[i+1]
                elif i == 5 :
                    single_facility_dict["vaccines_offered"] = temp_list[i]
                elif i == 7:
                    single_facility_dict["availability"] = temp_list[i]
        facility_list.append(single_facility_dict)
                    
    print(type(facility_list))
    print(len(facility_list))
    print(facility_list[0])
