# from urllib.request import urlretrieve as retrieve
#
# url = 'https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active'
#
# retrieve(url, 'vehicle.csv')
import kwargs as kwargs
import requests
import pandas as pd


def get_vehicles(*args):
    url = 'https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active'
    result = requests.get(url)

    # Convert to json
    df_json = result.json()
    return print(type(df_json))


get_vehicles()
