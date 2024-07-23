# Day 36 - July 23 '24
# Stock Price Tracker and SMS Notifier

import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
stocksApi = os.getenv('STOCKS_KEY')
newsAPI = os.getenv('NEWS_API')
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

stockSymbol = 'TSLA'
newsArticles = []
sendSMS = False
closes = []
opens = []

def getStockData():
    with requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stockSymbol}&apikey={stocksApi}') as response:
        response.raise_for_status()
        response = response.json()
        return response

def calcPriceDiff():
    diff = round(yesterdayClose - dayBeforeClose,2)
    diffPerc = round(100 * (diff/dayBeforeClose),1)
    return diffPerc

def getNews():
    with requests.get(f'https://newsapi.org/v2/top-headlines?q=tesla&pageSize=5&apiKey={newsAPI}') as response:
        response.raise_for_status()
        response = response.json()
        return response
    
def sendText(priceDifference, newsArticles):
    priceDifference_str = f'🔺{priceDifference}' if priceDifference > 0 else f'🔻{abs(priceDifference)}'
    for article in newsArticles:
        message = client.messages.create(
            body=f"""TSLA: {priceDifference_str}%
Headline: {article}""",
            from_="+1XXXXXXXX",
            to="+1XXXXXXXX",
        )

stocksData = getStockData()
timeSeries = stocksData["Time Series (Daily)"]

for date in timeSeries:
    closes.append(timeSeries[date]['4. close'])

yesterdayClose = float(closes[0])
dayBeforeClose = float(closes[1])

priceDifference = calcPriceDiff()

if abs(priceDifference) >= 5:
    news = getNews()
    newsArts = news['articles']
    newsArticles = [art['title'] for art in newsArts]
    sendText(priceDifference, newsArticles)
    