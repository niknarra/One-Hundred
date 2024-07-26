# Day 45 - July 26 '24
# Web Scraping with Beautiful Soup

from bs4 import BeautifulSoup
import requests

movies = []

siteData = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
siteData = siteData.text

webSoup = BeautifulSoup(siteData,'html.parser')

names = webSoup.find_all(name='h3',class_='title')

for name in names:
    movies.append(name.text)

with open('movies_list.txt',mode='w') as moviesFile:
    for name in movies[::-1]:
        moviesFile.write(f'{name}\n')
    