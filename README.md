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
    URL="https://vaccinefinder.nyc.gov/"
    APP_ENV="production"
    ZIP_CODE="10005"
2. Additionally, if the requirements files is not already present in repository or its missing when repository is cloned then create a requirements.txt file under the root folder and copy all the above mentioned packages' name into the file and save it

## Instructions
1. Use git client to clone or download this remote repository, [covid-vaccine-warrior](https://github.com/psk264/covid-vaccine-warrior/), on your local machine.  Note the location where it is cloned or downloaded
2. Use command line application to navigate to the location where this repository was cloned or downloaded.  Ensure that ``<base>`` from conda initialization is shown on cmd line.  If ``<base>`` is not shown then, before proceeding, run command:<br/>
```conda init bash```
3. Since this code uses specific packages like python-dotenv, it is recommended to create a new project specific anaconda virtual environment. Here we create virtual environment name "vaccine-warrior-env" using following command.  To create a environment with a different name, simply replace vaccine-warrior-env with desired name:<br/>
``` conda create -n vaccine-warrior-env python=3.8```
Note: The terminal may prompt for user input [y/n] during install, input Y and hit Enter
4. Activate the Anaconda environment "shopping-cart-env" using the command:<br/>
```conda activate vaccine-warrior-env```
5. After virtual environment is active i.e. ``<vaccine-warrior>`` is shown on command-line, then install the third-party package python-dotenv on this virtual environment using command:<br/>
 ```pip install -r requirements.txt```<br/>
**NOTE:** The requirements.txt file is already provided in the repository.
6. To ensure all packages are installed, you can list the packages using ```pip list``` 
7. After the setup is complete, depending on your preference on appraoches mentioned above, start the program using one of the following commands:<br/>
Run using command prompt:  ```python -m app.vaccine_warrior```   
Run a local web app:  ```FLASK_APP=web_app flask run```  <br/> 

## Additional Information
* The repository is integrated with the code climate: https://codeclimate.com/github/psk264/covid-vaccine-warrior
* The repository is integrated with the Travis CI: https://travis-ci.com/github/psk264/covid-vaccine-warrior
