import os
import json
import requests

BLS_API_KEY = os.environ.get('BLS_API_KEY')
BLS_ENDPOINT = "http://api.bls.gov/publicAPI/v2/timeseries/data/"


def fetch_bls_series(series, **kwargs):
    """
    Pass in a list of BLS timeseries to fetch data and return the series
    in JSON format. Arguments can also be provided as kwargs:

        - startyear (4 digit year)
        - endyear (4 digit year)
        - catalog (True or False)
        - calculations (True or False)
        - annualaverage (True or False)
        - registrationKey (api key from BLS website)

    If the registrationKey is not passed in, this function will use the
    BLS_API_KEY fetched from the environment.
    """

    if len(series) < 1 or len(series) > 25:
        raise ValueError("Must pass in between 1 and 25 series ids")

    # Create headers and payload post data
    headers = {'Content-Type': 'application/json'}
    payload = {
        'seriesid': series,
        'registrationKey': BLS_API_KEY,
    }

    # Update the payload with the keyword arguments and convert to JSON
    payload.update(kwargs)
    payload = json.dumps(payload)

    # Fetch the response from the BLS API
    response = requests.post(BLS_ENDPOINT, data=payload, headers=headers)
    response.raise_for_status()

    # Parse the JSON result
    result = response.json()
    if result['status'] != 'REQUEST_SUCCEEDED':
        raise Exception(result['message'][0])

    return result
