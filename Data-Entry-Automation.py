# Day 51 - August 6 '24
# Data Entry Automation using BeautifulSoup and Selenium WebDriver

import selenium
from bs4 import BeautifulSoup
import requests

MAX_RENT = 3000

getListings = requests.get('https://appbrewery.github.io/Zillow-Clone/')
getListings = getListings.text

webSoup = BeautifulSoup(getListings,'html.parser')

addresses = webSoup.select("div a address")
# links = webSoup.find_all("a",{"class":"StyledPropertyCardDataWrapper"}).get("href")

a_tag = webSoup.find('a', class_='StyledPropertyCardDataArea-anchor', attrs={'data-test': 'property-card-link'})

# Extract the href attribute
href_link = a_tag['href']

print(href_link)

# for link in links:
#     print(link.text)

# for address in addresses:
#     print(address.text)

# print(links)