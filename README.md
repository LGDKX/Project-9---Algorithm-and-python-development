# Project-9-Algorithm-and-python-development
During this project, we made a scrapping script and also the Connway's game of life.

The scrapping script is meant to scrap data from Instant Gaming (Games names and price), adding the TVA and compare it with the game on official store. For now, we are going to focus on Steam.

First we need to look to the website to see how it is done.

To begin with, we need the URLs. The URL to Instant Gaming website is : "https://www.instant-gaming.com/fr/"
As we want only the games on steam, we are going to the steam area. We now obtain "https://www.instant-gaming.com/fr/jeux/steam/"
There is one problem with this URL : If we change the page, it completly change. We obtain "https://www.instant-gaming.com/fr/rechercher/?type%5B0%5D=steam&page=2"
But if we go back on page 1 using the button at the button we obtain "https://www.instant-gaming.com/fr/rechercher/?type%5B0%5D=steam&page=1"
We now have our URL.

We can begin to code.
So first we import packages we need for now (maybe we will add some later)
We need BeautifulSoup as it is the package that allow us to scrap data and requests for we want to make web requests.