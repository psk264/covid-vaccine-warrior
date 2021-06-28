# Objective 
This repository contains the code for a COVID-19 vaccine finder within the five boroughs of New York City.  The code takes zip code as user input and list the top 10 closest facilities and shows its details (address, facility type, phone number, vaccine offered, availability).

# Features and Capabilities
* Website scrapping to gather data on NYC vaccination facilities 
* Execution through command line 
* Execution through web application (local)
* Execution through web application on web server through integration with Heroku 
* Code quality monitoring through integration with CodeClimate
* Continuous integration and testing through integration with Travis CI


# Prerequisite
* Anaconda 3.7+
* Python 3.7+
* Pip
* Git Bash
* Selenium

# Packages
* [python-dotenv](https://pypi.org/project/python-dotenv/) 
* [selenium](https://selenium-python.readthedocs.io/)
* [webdriver_manager](https://pypi.org/project/webdriver-manager/)
* [pgeocode](https://pypi.org/project/pgeocode/)
* [pandas](https://pandas.pydata.org/)
* [requests](https://docs.python-requests.org/)
* [uszipcode](https://pypi.org/project/uszipcode/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [mpu](https://mpu.readthedocs.io/)

# Setup
1. .env file
2. requirements file , if not already present in repo
3. # covid-vaccine-warrior

## Part I
#### Step 1: Navigate to the folder on your desktop


## Part II: Set up a new virtual environment
#### Step 1: Type "conda create -n vaccine-env python=3.8" + ENTER in the terminal application
#### Step 2: Type "y" + ENTER two times accept terminal conditions
#### Step 3: Type "conda activate vaccine-env" + ENTER 
#### Step 4: Type "conda init - bash"  + ENTER 

## Part III: Make sure your packages are installed
#### Step 1: Type "pip install -r requirements.txt" + ENTER into terminal
#### Step 2: Type "pip list" + ENTER into terminal

## Part IV: Run the Program
## In the command line type "python -m app.vaccine-finder" 
## In the command line type "python -m app.vaccine_warrior" 



# Instructions

# Additional Information
* The repository is integrated with the code climate: https://codeclimate.com/github/psk264/covid-vaccine-warrior
