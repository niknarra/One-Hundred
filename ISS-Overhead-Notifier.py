# Day 33 - July 13 '24
# ISS Overhead Notifier

import requests
import datetime as dt
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
my_email = os.getenv('my_email')
pwd = os.getenv('APP_PWD')

# Define location and time
myLocation = (17.385044, 78.486671)
time_now = dt.datetime.now()

# Define parameters for the sunrise-sunset API
params = {
    'lat': myLocation[0],
    'lng': myLocation[1],
    'formatted': 0
}

# Function to send an email notification
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='@yahoo.com',
            msg="Subject:ISS Overhead Notification\n\nLook Up!"
        )

# Get the current position of the ISS
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Check if your position is within +5 or -5 degrees of the ISS position
if (myLocation[0] - 5 <= iss_latitude <= myLocation[0] + 5) and (myLocation[1] - 5 <= iss_longitude <= myLocation[1] + 5):
    # Get the sunrise and sunset times
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()

    sunrise = dt.datetime.fromisoformat(data["results"]["sunrise"])
    sunset = dt.datetime.fromisoformat(data["results"]["sunset"])

    # Check if it is currently night time
    if time_now >= sunset or time_now <= sunrise:
        send_email()