# Insta Unfollowed List

I was inspired by Aaron Jack on YouTube to make this. I'd just learnt Python and was looking to exerise my new found skills and this is what came of it.

- This code will open a Chrome web browser, visit and login to [Instagram](https://www.instagram.com). 

- It'll then scan both your `followers` and `following` lists, do a compare and return the list of people who you are following but do not follow you back.

## Installation Process

- Clone this repository

- The packages required to run this code are listed in the `requirements.txt` file. 

- Open a terminal window, navigate to your project root folder and run `pip install -r ./requirements.txt` or `pipenv install -r ./requirements.txt` (if you're using a virtual environment).

- Don't forget to download a webdriver for your Chrome browser from here [Chrome WebDrivers](https://chromedriver.chromium.org/downloads). 

- You can either place the executable in the root of your project folder OR you can add it to your PATH.

- Edit `secrets.py` file to add your login password

- Edit `main.py` to add your username at the bottom of the file. 

## Executing the code

- Now that the setup is complete, you execute the code with `python main.py`

## Issues

- Beware that the website is constantly changing so some of the page elements may no longer apply. You may need to make some adjustments to get it working again.
