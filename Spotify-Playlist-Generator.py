# Day 46 - July 26 '24
# Spotify Playlist generator with Web Scraping

import datetime
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
clientID = os.getenv('SP_CLIENT_ID')
clientSecret = os.getenv('SP_CLIENT_SECRET')
date = input("Which date do you want to travel to? Type the date in YYYY-MM-DD format: ")

billboard_url = f'https://www.billboard.com/charts/hot-100/{date}'

getSongs = requests.get(billboard_url)
getSongs = getSongs.text

webSoup = BeautifulSoup(getSongs,'html.parser')

songs = webSoup.select("li ul li h3")
songsList = []

for song in songs:
    songsList.append(song.text.strip())
    
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
                                           client_secret=clientSecret,
                                           redirect_uri='http://localhost:4304/auth/spotify/callback',
                                           scope="playlist-modify-private",
                                         ))

results = sp.current_user()
USER_ID = results['id']

uris = [sp.search(title)['tracks']['items'][0]['uri'] for title in songs]

PLAYLIST_ID = sp.user_playlist_create(user=USER_ID,public=False,name=f"{date} BillBoard-100")['id']
sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=uris,user=USER_ID)
