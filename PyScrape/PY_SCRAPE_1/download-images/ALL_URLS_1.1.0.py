# via https://stackoverflow.com/questions/24342186/get-all-urls-from-a-website-using-python

#!/usr/bin/python
import urllib2
import urlparse
from BeautifulSoup import BeautifulSoup

def getAllUrl(url):
urlList = []
try:
    page = urllib2.urlopen( url ).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    for anchor in soup.findAll('a', href=True):
        if not 'http://' in anchor['href']:
            if urlparse.urljoin('http://bobthemac.com', anchor['href']) not in urlList:
                urlList.append(urlparse.urljoin('http://bobthemac.com', anchor['href']))
        else:
            if anchor['href'] not in urlList:
                urlList.append(anchor['href'])

    return urlList

except urllib2.HTTPError, e:
    urlList.append( e )

if __name__ == "__main__":
urls = getAllUrl('http://bobthemac.com')

fullList = []

for x in urls:
    listUrls = list
    listUrls = getAllUrl(x)
    try:
        for i in listUrls:
            if not i in fullList:
                fullList.append(i)
    except TypeError, e:
        print 'Woops wrong content passed'

for i in fullList:
    print i
