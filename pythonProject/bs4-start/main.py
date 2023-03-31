from bs4 import BeautifulSoup
import requests
from pprint import pprint



response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_tr_tags = soup.find_all(name="tr", class_="athing")
rss_list = []
for tr in all_tr_tags:
    article = tr.find(name="span", class_="titleline")
    article_link = article.find(name="a")['href']
    article_preview = article.getText()
    article_info = {
        "article_preview": article_preview,
        "article_link": article_link,
        "article_votes": 0
    }
    rss_list.append(article_info)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

for rss in rss_list:
    rss["article_votes"] = article_upvotes[rss_list.index(rss)]


pprint(rss_list)