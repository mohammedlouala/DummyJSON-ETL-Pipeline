import requests
import pandas as pd

BASE_URL = 'https://dummyjson.com/'

def extract(table_name):
    """Extract data from a DummyJSON Endpoint and return a DataFrame. """
    url = f'{BASE_URL}/{table_name}?limit=0'

    response = requests.get(
        url,
        timeout=30
    )
    response.raise_for_status()

    data = response.json()
    records = data[table_name]

    return pd.json_normalize(records)
