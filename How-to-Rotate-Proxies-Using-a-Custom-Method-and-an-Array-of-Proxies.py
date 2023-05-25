# import packages  
import requests  
from bs4 import BeautifulSoup  
import random  
  
# List of proxies  
proxies = [  
    "proxyprovider1.com:2010", "proxyprovider1.com:2020",  
    "proxyprovider1.com:2030", "proxyprovider2.com:2040",  
    "proxyprovider2.com:2050", "proxyprovider2.com:2060",  
    "proxyprovider3.com:2070", "proxyprovider3.com:2080",  
    "proxyprovider3.com:2090"  
]  
  
  
# Custom method to rotate proxies  
def get_proxy():  
    # Choose a random proxy from the list  
    proxy = random.choice(proxies)  
    # Return a dictionary with the proxy for both http and https protocols  
    return {'http': proxy, 'https': proxy}  
  
  
# Send requests using rotated proxies  
for i in range(10):  
    # Set the URL to scrape  
    url = 'https://brightdata.com/'  
    try:  
        # Send a GET request with a randomly chosen proxy  
        response = requests.get(url, proxies=get_proxy())  
  
        # Use BeautifulSoup to parse the HTML content of the website.  
        soup = BeautifulSoup(response.content, "html.parser")  
  
        # Find all the links on the website.  
        links = soup.find_all("a")  
  
        # Print all the links.  
        for link in links:  
            print(link.get("href"))  
    except requests.exceptions.RequestException as e:  
        # Handle any exceptions that may occur during the request  
        print(e)
