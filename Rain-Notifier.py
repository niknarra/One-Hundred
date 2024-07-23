# Day 35 - July 22 '24
# Automated Rain Notifier

import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()
weather_key = os.getenv('weather_key')
lat = os.getenv('lat')
long = os.getenv('long')
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

willRain = False

def sendText():
    message = client.messages.create(
    body="Bring an Umbrella! It might be raining.",
    from_="+1XXXXXXXX",
    to="+1XXXXXXXX",
)

def getCurrentWeather(lat,long,key):
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&cnt=4&appid={key}')
    weather.raise_for_status()
    weather_data = weather.json()
    return weather_data

weatherForecast = getCurrentWeather(lat=lat,long=long,key=weather_key)
currentWeatherCondition = weatherForecast['weather'][0]['id']

if currentWeatherCondition < 700:
    willRain = True
    
if willRain:
    sendText()