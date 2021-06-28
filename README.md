# Group Project by team Violet Python, NYU Stern, Summer 2021

## Objective 
This repository contains the code for a COVID-19 vaccine finder within the five boroughs of New York City.  The code takes zip code as user input and list the top 10 closest facilities and shows its details (address, facility type, phone number, vaccine offered, availability).

## Features and Capabilities
* Website scrapping to gather data on NYC vaccination facilities 
* Execution through command line 
* Execution through web application (local)
* Execution through web application on web server through integration with Heroku 
* Code quality monitoring through integration with CodeClimate
* Continuous integration and testing through integration with Travis CI


## Prerequisite
* Anaconda 3.7+
* Python 3.7+
* Pip
* Git Bash
* Selenium

## Packages
* [python-dotenv](https://pypi.org/project/python-dotenv/) 
* [selenium](https://selenium-python.readthedocs.io/)
* [webdriver_manager](https://pypi.org/project/webdriver-manager/)
* [pgeocode](https://pypi.org/project/pgeocode/)
* [pandas](https://pandas.pydata.org/)
* [requests](https://docs.python-requests.org/)
* [uszipcode](https://pypi.org/project/uszipcode/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [mpu](https://mpu.readthedocs.io/)

## Setup
1. In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify following information:
```   
    URL="https://vaccinefinder.nyc.gov/"
    APP_ENV="production"
    ZIP_CODE="10005"
```    
2. Additionally, if the requirements files is not already present in repository or its missing when repository is cloned then create a requirements.txt file under the root folder and copy all the above mentioned packages' name into the file and save it
3. Use git client to clone or download this remote repository, [covid-vaccine-warrior](https://github.com/psk264/covid-vaccine-warrior/), on your local machine.  Note the location where it is cloned or downloaded
4. Use command line application to navigate to the location where this repository was cloned or downloaded.  Ensure that ``<base>`` from conda initialization is shown on cmd line.  If ``<base>`` is not shown then, before proceeding, run command:<br/>
```conda init bash```
5. Since this code uses specific packages like python-dotenv, it is recommended to create a new project specific anaconda virtual environment. Here we create virtual environment name "vaccine-warrior-env" using following command.  To create a environment with a different name, simply replace vaccine-warrior-env with desired name:<br/>
``` conda create -n vaccine-warrior-env python=3.8```
Note: The terminal may prompt for user input [y/n] during install, input Y and hit Enter
6. Activate the Anaconda environment "shopping-cart-env" using the command:<br/>
```conda activate vaccine-warrior-env```
7. After virtual environment is active i.e. ``<vaccine-warrior>`` is shown on command-line, then install the third-party package python-dotenv on this virtual environment using command:<br/>
 ```pip install -r requirements.txt```<br/>
**NOTE:** The requirements.txt file is already provided in the repository.
8. To ensure all packages are installed, you can list the packages using ```pip list```

## Instructions
After above mentioned setup is complete, depending on your preference on appraoches mentioned above, start the program using one of the following commands:<br/>
1. Run using command prompt: <br/>  ```python -m app.vaccine_warrior```   
   1. After using above command, the script invoke the chromedriver to open chrome browser and navigate to the URL set in env file.  It will take some time to gather all the HTML element using scraping function and convert the relevant information into a list of dictionaries <br/>
   2. Terminal will then prompt for user input of valid US zip code <br/>
   3. When user inputs the valid US zip code, the program will calculate the distance of input zipcode with all the zipcodes in the list of dictionaries.  This distance is then stored in the list and sorted <br/>
   4. The top 10 records from the sorted list is displayed as the closest facilities <br/>
**NOTE:** The code is equipped to handle error scenarios like invalid zip code, random string instead of zip code, longer or shorter than 5-digit zip code
2. Run a local web app:  <br/> 
        ````# Mac OS: 
            FLASK_APP=web_app flask run
            # Windows OS:
            # ... if `export` doesn't work for you, try `set` instead
            export FLASK_APP=web_app 
            flask run ````
            
    1. Using above command, the program will go through the initial steps as mentioned in 1.  Enter the valid zip code in command line when prompted to move on to web app code
    2. After successful message, the web application will be accessible at http://127.0.0.1:5000  or http://localhost:5000
  
  
 

## Additional Information
* The repository is integrated with the code climate: https://codeclimate.com/github/psk264/covid-vaccine-warrior
* The repository is integrated with the Travis CI: https://travis-ci.com/github/psk264/covid-vaccine-warrior
