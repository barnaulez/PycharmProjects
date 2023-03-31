import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
empire_moovies = response.text

soup = BeautifulSoup(empire_moovies, "html.parser")
content_div = soup.find(name="div", class_="listicle-container")
contents = content_div.find_all(name="img", class_="jsx-2590794431 loading")

moovies_temp = [content.get("alt") for content in contents]
moovies_list = list(reversed(moovies_temp))

for moovie in moovies_list:
    moovies_list[moovies_list.index(moovie)] = f"{moovies_list.index(moovie) + 1}) {moovie}"

with open("moovies.txt", mode="w") as f:
    for moovie in moovies_list:
        f.write(f"{moovie}\n")


