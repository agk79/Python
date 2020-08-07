# BLS API v1 url
base_url = 'https://api.bls.gov/publicAPI/v1/timeseries/data/'

# BLS series id for the civilian labor force participation rate
series = {'id': 'LNS11300000',
          'name': 'Labor Force Participation Rate'}

data_url = '{}{}'.format(base_url, series['id'])
print(data_url)


import requests

r = requests.get(data_url).json()
print('Status: ' + r['status'])
