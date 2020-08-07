import csv
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

# CSV PRINT
csv_file = open('test1.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['href', 'title'])

# URL IMPORT
with open('/Users/akarl/Box/Python/PYTHON_CDF/urls.csv') as inf:
    urls = (line.strip() for line in inf)
    for url in urls:
        site = urlopen(url)
        soup = BeautifulSoup(site, "html.parser")

# VALUES IN CSV OUTPUT
        for links in soup.find_all('ul', {'class': 'fab-primary-nav'}):
            domain = "victoriassecret.com"
            base = "http://victoriassecret.com"
            for ul in links.find_all('ul'):
                columnid = ul.get('aria-labelledby')
                for a in links.find_all('a'):
                    title = a.text
                    print(title)
                    href = a.get('href')
                    print(href)
                    combined = title + '(' + href + ')'
                    print(combined)
                    print(columnid)
                    csv_writer.writerow([title, href, combined, columnid])
csv_file.close()