
import os

import requests

# COVID_URL = "http://coronavirusapi.com/getTimeSeries/ny"
# resp = requests.get(COVID_URL)
# print(resp.text)

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': os.getenv('COVID_API_KEY')
    }

response = requests.request("GET", url, headers=headers)

data = response.json()["response"]

for c in data:
    print(c)