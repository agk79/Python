import os
import urllib
import urllib2


baseUrl = "http://filmygyan.in/wp-content/gallery/katrina-kaifs-top-10-"\
      "cutest-pics-gallery/cute%s.jpg"

for i in range(1,11):
    url = baseUrl % i
    urllib.urlretrieve(url, os.path.basename(url))
