
import datetime
import json
import time
import requests
from cachetools import cached, TTLCache

DATA_URL = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"

cache = TTLCache(maxsize=100, ttl=3600)

@cached(cache)
def get_state_data(state) -> None:

    print("Fetching Data from GitHub.....")
    result = {}
    r = requests.get(DATA_URL, allow_redirects=True)

    for l in r.text.split('\n')[1:]:

        dt,s,f,c,d = l.split(',')
        s = s.lower()
        if not result.get(s):
            result[s] = {}
        result[s].update(
            {

                dt: {
                    "fips": f,
                    "cases": c,
                    "deaths": d
                }
            })

    return result[state]
#
