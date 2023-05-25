# import packages.  
import requests  
from bs4 import BeautifulSoup  
  
# Define a link to the web page.  
url = "https://brightdata.com/"  
  
# Send a GET request to the website.  
response = requests.get(url)  
  
# Use BeautifulSoup to parse the HTML content of the website.  
soup = BeautifulSoup(response.content, "html.parser")  
  
# Find all the links on the website.  
links = soup.find_all("a")  
  
# Print all the links.  
for link in links:  
    print(link.get("href"))
