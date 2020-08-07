# importing the libraries
from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
print(soup.prettify())  # print the parsed data of html


# Example 1:

# Let’s just first print the title of the webpage.
print(soup.title)
