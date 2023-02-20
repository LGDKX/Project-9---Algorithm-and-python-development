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

###########################################################
# Import csv package in order to send data into csv files #
###########################################################
# import csv

#########################################################
# Import re package in order to use regular expressions #
#########################################################
# import re

# List of excluded words
exclude_list = ['PC', 'Playstation', 'Xbox', 'Nintendo']

# User-Agent header to simulate a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}




    
def fetch_data():
    # Loop through pages 1 to 134
    for page in range(1, 2):
        # Base URL that will change at every turn of the loop
        url = f"https://www.instant-gaming.com/fr/rechercher/?type%5B0%5D=steam&page={page}" #pylint: disable=all    
        
        # Fetch the page
        result = requests.get(url, headers=headers)
        doc = BeautifulSoup(result.text, "html.parser")

        # Fetch the games pages's link
        links = doc.find_all("a", class_="cover")

        # Fetch the games's title
        titles = doc.find_all("span", class_="title")

        #Fetch the games's price
        prices = doc.find_all("div", class_="price")     
            
def print_data(links, titles, prices):
    # Print the links
    for link in links:
        print(link.get("href"))

    #Print the titles
    for title in titles:
        # Exclude the parasitic titles
        if not any(word in title.text for word in exclude_list):
            print(title.text)

    # Print the prices with 20% added
    for price in prices[1:]:
        # Convert the price to a float value
        price_value = float(price.text.replace(',', '.').split('€')[0])
        # Add 20% to the price and format the result as a string with two decimal places
        tva_price = '{:.2f} €'.format(price_value * 1.2)
        print(tva_price)

def execute():
    fetch_data
    print_data

execute