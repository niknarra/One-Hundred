# Day 51 - August 4 '24
# Automated Speed Test and Tweeter

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

# Replace these with your actual thresholds
actualDownload = 100
actualUpload = 50

# Twitter API credentials
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('your_access_token')
ACCESS_TOKEN_SECRET = os.getenv('your_access_token_secret')

def postTweet(download, upload):
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweet = f"Internet speed is below the expected threshold. Download: {download} Mbps, Upload: {upload} Mbps."
    api.update_status(status=tweet)
    print("Tweeted: " + tweet)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(url='https://www.speedtest.net')

# Click on the Go button to start the speed test
goBtn = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
goBtn.click()

# Wait for the test to complete
time.sleep(60)

# Retrieve the download and upload speeds
downloadRate = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
uploadRate = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

# Convert the speeds to float for comparison
downloadRate = float(downloadRate)
uploadRate = float(uploadRate)

if downloadRate < actualDownload or uploadRate < actualUpload:
    postTweet(downloadRate, uploadRate)

driver.quit()
