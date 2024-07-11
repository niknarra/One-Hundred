# Day 32 - July 12 '24
# Automated Birthday Wisher

import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import random
import pandas as pd

# Function to generate the personalized letter content
def generateLetter(name):
    letterNum = random.randint(1,3)
    with open(f'letter_templates/letter_{letterNum}.txt', mode='r') as letter:
        content = letter.read()
    return content.replace('[NAME]', name)

# Function to email the generated letter
def emailLetter(name, email, letter_content):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{letter_content}"
        )

# Setting up credentials
load_dotenv()
my_email = os.getenv('my_email')
pwd = os.getenv('APP_PWD')

# Reading and getting the list of birthdays from the csv
birthdays = pd.read_csv('birthdays.csv')
birthdaysDict = birthdays.to_dict(orient='records')

# Getting todays day and month
today = dt.datetime.now()
date = (today.month, today.day)

# Getting the names and emails of people celebrating their birthday today
todaysBirthdays = {birthday['name']: birthday['email'] for birthday in birthdaysDict if birthday['month'] == date[0] and birthday['day'] == date[1]}

# Looping over the names in the list of birthdays today
for name, email in todaysBirthdays.items():
    letter_content = generateLetter(name)
    emailLetter(name, email, letter_content)