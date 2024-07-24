# Day 38 - July 23 '24
# Workout Tracker with Google Sheets

import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()
nutAppID = os.getenv('NUT_APP_ID')
nutAppKey = os.getenv('NUT_APP_KEY')

today = datetime.datetime.now()
date_string = today.strftime("%d/%m/%Y")
time_string = today.strftime("%X")

query = input("What exercise did you do today? ")

sheety_endpoint = 'https://api.sheety.co/b134f85701fc38a0bf86706af9bd1da2/exerciseTracker/workouts'

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
nutritionix_params = {
    'query':query,
}
nutritionix_headers = {
    'x-app-id':nutAppID,
    'x-app-key':nutAppKey
}
sheety_headers = {
    'Authorization': os.getenv('SHEETY_KEY')
}

workoutDetails = requests.post(url=nutritionix_endpoint,json=nutritionix_params,headers=nutritionix_headers)
workoutDetails.raise_for_status()
workouts = workoutDetails.json()
exercises = workouts['exercises']

for workout in exercises:
    exercise = workout['name']
    duration = workout['duration_min']
    calories = workout['nf_calories']
    
    sheety_data = {
        "workout": {
            "date": date_string,
            "time": time_string,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }
    
    sheet = requests.post(url=sheety_endpoint,json=sheety_data,headers=sheety_headers)
    sheet.raise_for_status()