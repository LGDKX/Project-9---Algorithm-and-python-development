"""Scrapping script to get all the prices on Instant Gaming with TVA added
"""

###########################################################################
# Import the InstantGamingScraper class to scrap data from Instant Gaming #
###########################################################################
from scrapper import InstantGamingScraper

####################################################################
# Import the DataSearcher class to search for games among our data #
####################################################################
from scrapper import DataSearcher

# Ask whether if you want to search for a game or to scrap the website
choice = input('Veux-tu rechercher une entrée existante (Taper "Rechercher") \
ou récuperer les données sur le site (Taper "Recuperer") ? ')
if choice.lower() == "rechercher":
    # Ask the game title
    query = input("Entrez le nom du jeu à chercher : ")
    # Create an instance of the DataSearcher class
    game = DataSearcher(query)
    # Call the search function on the instance to start the search process
    game.search(query)
elif choice.lower() == "recuperer":
    # Create an instance of the InstantGamingScraper class
    scraper = InstantGamingScraper(num_pages=int(input("Combien de pages doivent \
êtres analysés ? : ")))
    # Call the execute() method on the instance to start the scraping process
    scraper.execute_scrap()
else:
    print('Choix invalide, merci de taper "Rechercher" ou "Recuperer"')
