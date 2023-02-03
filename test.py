from bs4 import BeautifulSoup
import requests

# Website URL
url = "https://www.instant-gaming.com/fr/jeux/steam/"

# User-Agent header to simulate a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Fetch the page
result = requests.get(url, headers=headers)
doc = BeautifulSoup(result.text, "html.parser")

# Find all the links on the page
links = doc.find_all("a")

# Iterate through all the links and check if it contains "acheter"
for link in links:
    if "acheter" in link.get("href"):
        print(link.get("href"))