# Day 47 - July 27 '24
# Automated Amazon Price Tracker with Web Scraping

import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
buyPrice = 100
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
my_email = os.getenv('my_email')
pwd = os.getenv('APP_PWD')
email = '@example.com'
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
#     "Accept-Encoding": "gzip, deflate, br", 
#     "Accept-Language": "en-US,en;q=0.9", 
#     "Sec-Fetch-Dest": "document", 
#     "Sec-Fetch-Mode": "navigate", 
#     "Sec-Fetch-Site": "none", 
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15", 
#   }

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# siteData = requests.get('https://appbrewery.github.io/instant_pot/',headers=headers)
siteData = requests.get(url,headers=header)
siteData.raise_for_status()
siteData = siteData.text

webSoup = BeautifulSoup(siteData,'html.parser')
#print(webSoup.prettify())
productName = webSoup.find(name='span',id='productTitle').text

def getCurrentPrice():
    priceWhole = webSoup.find(name='span',class_='a-price-whole')
    priceFrac = webSoup.find(name='span',class_='a-price-fraction')
    finalPrice = float(priceWhole.text)+(float(priceFrac.text)/100)
    
    return finalPrice

def sendAlert():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Amazon Price Alert for {productName}!"
        )

currentPrice = getCurrentPrice()

if currentPrice < buyPrice:
    sendAlert()