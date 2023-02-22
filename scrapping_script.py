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

##################################################################
# Import pandas package in order to manipulate data in csv files #
##################################################################
import pandas as pd

# User-Agent header to simulate a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
    
def fetch_data():
    # Create empty lists to store the scraped data
    links = []
    titles = []
    prices = []

    # List of excluded words
    exclude_list = ['PC', 'Playstation', 'Xbox', 'Nintendo']
    
    # Loop through pages 1 to 134
    for page in range(1, 135):
        # Base URL that will change at every turn of the loop
        url = f"https://www.instant-gaming.com/fr/rechercher/?type%5B0%5D=steam&page={page}" #pylint: disable=all    
        
        # Fetch the page
        result = requests.get(url, headers=headers)
        doc = BeautifulSoup(result.text, "html.parser")

        # Fetch the games pages's link
        links += [link.get("href") for link in doc.find_all("a", class_="cover")]

        # Fetch the games's title
        titles += [title.text for title in doc.find_all("span", class_="title") if not any(word in title.text.split() for word in exclude_list)]


        #Fetch the games's price
        prices += [float(price.text.replace(',', '.').split('€')[0]) for price in doc.find_all("div", class_="price")[1:]]

        print(f"Page {page}: titles={len(titles)}, prices={len(prices)}, links={len(links)}")

    # Add 20% to the prices
    prices = [round(price * 1.2, 2) for price in prices]

    return titles, prices, links
           
def save_to_csv(titles, prices, links):
    # Create a pandas DataFrame from the scraped data
    data = {'Title': titles, 'Price': prices, 'Link': links}
    df = pd.DataFrame(data)
    
    # Save the DataFrame to a CSV file
    df.to_csv('game_prices.csv', index=False)
    print('Data saved to game_prices.csv')

def execute():
    titles, prices, links, = fetch_data()
    save_to_csv(titles, prices, links,)

execute()