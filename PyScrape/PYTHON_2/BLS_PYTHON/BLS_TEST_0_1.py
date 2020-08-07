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