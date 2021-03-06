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
print(r.keys())

r = r['Results']['series'][0]['data']
print(r[0])

import pandas as pd

dates = ['{} {}'.format(i['period'], i['year']) for i in r]
index = pd.to_datetime(dates)
data = {series['id']: [float(i['value']) for i in r],
        'footnotes': [i['footnotes'][0] for i in r]}

df = pd.DataFrame(index=index, data=data).iloc[::-1]

df.tail(3)

%matplotlib inline

df['mean'] = df[series['id']].mean()
df[[series['id'], 'mean']].plot(title=series['name'])



# Example 2: Requesting multiple series and specific dates
# The second examples uses the BLS API v2 (which requires free registration) to request more than one series at the same time. The version 2 API has a higher daily query limit, allows more years and series to be returned in each query, and allows some additional options such as requesting data in percent change rather than level. See difference between v1 and v2.

# Parameters
# The new url, registration key, and data parameters are shown below.

import config # .py file with bls_key = 'API key here'

# The url for BLS API v2
url = 'https://api.bls.gov/publicAPI/v2/timeseries/data/'

# API key in config.py which contains: bls_key = 'key'
key = '?registrationkey={}'.format(config.bls_key)

# Series stored as a dictionary
series_dict = {
    'LNS14000003': 'White',
    'LNS14000006': 'Black',
    'LNS14000009': 'Hispanic'}

# Start year and end year
dates = ('2008', '2017')