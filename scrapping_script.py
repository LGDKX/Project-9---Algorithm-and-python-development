"""Scrapping script to compare game price between official website such as steam and Instant Gaming.
"""

###############################################
# Import BeautifulSoup in order to scrap data #
###############################################
from bs4 import BeautifulSoup


#########################################################
# Import requests package in order to make web requests #
#########################################################
import requests

# Website URL
url = "https://www.instant-gaming.com/fr/jeux/steam/" #pylint: disable=all

# User-Agent header to simulate a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Fetch the page
result = requests.get(url, headers=headers)
doc = BeautifulSoup(result.text, "html.parser")

# Fetch the game's title and price
title = doc.find("h1")
price = doc.find("div", class_="total")

# Print the game's title without html code
for title in title:
    print(title.strip())

# Print the game's price without html code and by adding the TVA (The real price in short)
for price in price:
    # Remove the html code and the € symbol
    price = float(price.strip().replace("€", ""))
    # Add the 20 % TVA Tax
    real_price = price * 1.20
    # Print the price
    print("Price : {:.2f} €".format(real_price))
