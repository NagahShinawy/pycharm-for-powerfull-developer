"""
created by Nagaj at 20/04/2021
"""

import json
import os

import requests

token = os.environ.get("token")
credentials = dict(token=token)

WEATHER_ENDPOINT = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=ZIP:28801&startdate=2010-05-01&enddate=2010-05-01"

response = requests.get(WEATHER_ENDPOINT, headers=credentials)

if response.status_code == 200:
    with open(os.path.join(os.getcwd(), "weather.json"), 'w') as f:
        json.dump(response.json(), f, indent=4)
