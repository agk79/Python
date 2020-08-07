#via https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

#Python program to scrape website
#and save quotes from website

# import requests 
# URL = "https://www.geeksforgeeks.org/data-structures/"
# r = requests.get(URL) 
# print(r.content) 


#This will not run on online IDE 
import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify()) 
