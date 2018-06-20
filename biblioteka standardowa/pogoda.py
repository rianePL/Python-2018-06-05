# https://www.metaweather.com/api/location/search/?query=Warsaw
# https://www.metaweather.com/api/location/523920/

# zapytać o nazwę miasta
# wkleić nazwę miasta do pierwszego linku
# odczytać z tamtej strony dane json
# "woeid"
# wkleić kod lokacji do drugiego linku
# wypisać dane z tej drugiej strony

import urllib.request
import json

SEARCH_URL = 'https://www.metaweather.com/api/location/search/'
LOCATION_URL = 'https://www.metaweather.com/api/location/'

location_name = input('podaj nazwę miasta: ')
with urllib.request.urlopen(SEARCH_URL + '?query=' + location_name) as response:
    location_string = response.read().decode('utf-8')

location_data = json.loads(location_string)
location_id = location_data[0]["woeid"]

with urllib.request.urlopen(LOCATION_URL + str(location_id) + '/') as response:
    weather_string = response.read().decode('utf-8')

weather_data = json.loads(weather_string)
print(weather_data["consolidated_weather"][0]["the_temp"])

# nowsza biblioteka
# import requests
# location_data = requests.get(SEARCH_URL, params={'query':location_name}).json()