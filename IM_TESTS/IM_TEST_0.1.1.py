# import requests

# url = 'http://google.com/favicon.ico'
# r = requests.get(url, allow_redirects=True)
# open('google.ico', 'wb').write(r.content)

import requests

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True

print is_downloadable('https://www.youtube.com/watch?v=9bZkp7q19f0')
# >> False
print is_downloadable('http://google.com/favicon.ico')
# >> True