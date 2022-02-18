import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")


for article in articles:
    title = article.find("a").get_text()
    url = article.find("a")["href"]
    date = article.find("time")["datetime"]
    print(title, url, date)