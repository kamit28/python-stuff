'''
Created on 7 Mar. 2018

@author: Amit.Kumar1
'''

import requests
import sys

req_params = []
print("Program to get weather data for given geographical coordinates or ZIP code")
print("If Zip Code is chosen and country is not provided, country will default to US")
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"
strategy = input("Please input 1 for geograhical coordinates and 2 for Zip Code: ")
if int(strategy) == 1:
    try:
        lat = float(input("Please input the latitude: "))
        lon = float(input("Please input the longitude: "))
        req_params.append(('lat', lat))
        req_params.append(('lon', lon))
    except ValueError as ve:
        print("your inputs were not valid coordinates!")
elif int(strategy) == 2:
    try:
        zip_code = input("Please input the ZIP Code: ")
        int(zip_code)
        country = input("Please enter the 2-character ISO country code: ")
        req_params.append(('zip', zip_code + ',' + country))
    except ValueError as ve:
        print("your inputs was not a valid ZIP code!")
else:
    print("Invalid input!")
    sys.exit()
req_params.append(('APPID', 'e684cf310dc4596179d1bece642591b3'))
weather_response = requests.get(weather_api_url, params=req_params)
print(weather_response.url)
if weather_response.status_code == 200:
    cont_type, the_charset = weather_response.headers['content-type'].split(';')
    
    if cont_type == 'application/json':
        print(weather_response.json())
    else:
        print(weather_response.text)
elif weather_response.status_code == 400:
    print("Bad request")
elif weather_response.status_code == 404:
    print("Content not found")
elif weather_response.status_code == 500:
    print("Internal server error")
else:
    print(weather_response.text)

    