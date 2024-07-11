# Day 32 - July 12 '24
# Monday Motivational Quote sender with SMTP

import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import random

load_dotenv()

# Setting up credentials
my_email = os.getenv('my_email')
pwd = os.getenv('APP_PWD')

# Getting the day of the week
now = dt.datetime.now()
today = now.weekday()

# Function to generate a random quote
def getQuote():
    with open('quotes.txt',mode='r') as quotes:
        quotesList = quotes.readlines()
        todaysQuote = random.choice(quotesList)
        return todaysQuote
    
# Function to setup SMTP and send the email
def sendEmail():
    quote = getQuote()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="@gmail.com",
            msg=f'Subject:Quote of the week\nHello,\n {quote}'
            )

# Send the email only on Mondays     
if today == 0:
    sendEmail()