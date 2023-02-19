"""Scrapping script to compare game price between official website such as steam and Instant Gaming.
"""

####################################################
# Import BeautifulSoup in order to fetch HTML code #
####################################################
from bs4 import BeautifulSoup

#########################################################
# Import requests package in order to make web requests #
#########################################################
import requests

#########################################################
# Import re package in order to use regular expressions #
#########################################################
# import re

# Loop through pages 1 to 134
for page in range(1, 3):
    # Base URL that will change at every turn of the loop
    url = f"https://www.instant-gaming.com/fr/rechercher/?type%5B0%5D=steam&page={page}" #pylint: disable=all

    # User-Agent header to simulate a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Fetch the page
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, "html.parser")

    links = doc.find_all("a", class_="cover")
    titles = doc.find_all("span", class_="title")

    for link in links:
        print(link.get("href"))

    for title in titles:
        print(title.text)