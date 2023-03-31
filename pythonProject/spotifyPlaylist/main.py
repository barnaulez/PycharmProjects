from bs4 import BeautifulSoup
import requests
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from pprint import pprint


today = datetime.now()
y = str(today.year - 59)
m = str(today.month) if today.month>=10 else f"0{today.month}"
d = str(today.day) if today.day>=10 else f"0{today.day}"
url = f"https://www.billboard.com/charts/hot-100/{y}-{m}-{d}"
print(url)

response = requests.get(url)
chart_page = response.text

soup = BeautifulSoup(chart_page, "html.parser")

#playlist's name. the name of playlist is the name of chart. Every sunday new chart
pl_title = soup.find(name="div", class_="chart-results").find(name="p", class_="c-tagline").getText()


chart_list_tags = soup.find(name="div", class_="chart-results").find_all(name="div", class_="o-chart-results-list-row-container")
chart_list = []

for tag in chart_list_tags:
    title_tag = tag.find(name="h3", id="title-of-a-story")
    title = title_tag.getText().strip()
    artist = title_tag.find_next(name="span").getText().strip()
    track = {
        "artist": artist,
        "title": title
    }
    chart_list.append(track)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
                                               client_secret=os.environ.get("SPOTIFY_SECRET"),
                                               redirect_uri="http://example.com",
                                               scope="user-library-modify"))


#-------searching track in spotify
def search_track():
    pass

q = f"track: {chart_list[1]['artist']}-{chart_list[1]['title']}"
search_list_raw = sp.search(q, limit=50, type="track")
search_list = search_list_raw['tracks']['items']
#pprint(search_list[0])
search_list_sorted = sorted(search_list, key=lambda d: d['album']['release_date'])

indexes_to_delete = []
for i in range(len(search_list_sorted)):
    info = search_list_sorted[i]
    print(type(info))
    if (info['album']['album_type'] == 'compilation') or (info['album']['artists'][0]['name'] != 'The Beatles'):
        print(info['album']['album_type'])
        print(info['album']['artists'][0]['name'])
        print(info['album']['name'])
        print("###################################")

pprint(len(search_list_sorted))
#pprint(search_list_sorted)
print(indexes_to_delete)