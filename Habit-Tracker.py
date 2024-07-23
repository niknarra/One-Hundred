# Day 37 - July 23 '24
# Habit Tracker with Pixela

import requests
import os
import dotenv
from dotenv import load_dotenv
import datetime

load_dotenv()
username = os.getenv('PIXELA_USERNAME')
pixelaKey = os.getenv('PIXELA_KEY')
today = datetime.datetime.now()
today = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":pixelaKey, 
    "username":"niknarra", 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
    }

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

graph_params = {
    'id':"nikgraph0",
    'name':"Nik's Coding Graph",
    'unit':'minutes',
    'type':'float',
    'color':'ajisai'
}

headers = {
    'X-USER-TOKEN':pixelaKey
}

# response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)

pixel_endpoint = f'{graph_endpoint}/nikgraph0'

pixel_params = {
    'date': today,
    'quantity': '1'
}

#response = requests.post(url=pixel_endpoint,json=pixel_params,headers=headers)
