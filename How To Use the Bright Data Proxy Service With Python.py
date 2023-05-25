import requests  
from bs4 import BeautifulSoup  
import random  
  
# Define parameters provided by Brightdata  
host = 'zproxy.lum-superproxy.io'  
port = 22225  
username = 'username'  
password = 'password'  
session_id = random.random()  
  
# format your proxy  
proxy_url = ('http://{}-session-{}:{}@{}:{}'.format(username, session_id,  
                                                     password, host, port))  
  
# define your proxies in dictionary  
proxies = {'http': proxy_url, 'https': proxy_url}  
  
# Send a GET request to the website  
url = "https://brightdata.com/"  
response = requests.get(url, proxies=proxies)  
  
# Use BeautifulSoup to parse the HTML content of the website  
soup = BeautifulSoup(response.content, "html.parser")  
  
# Find all the links on the website  
links = soup.find_all("a")  
  
# Print all the links  
for link in links:  
    print(link.get("href"))
