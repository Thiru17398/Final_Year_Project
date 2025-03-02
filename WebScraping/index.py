import requests
from bs4 import BeautifulSoup
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# payload = { 'api_key': 'ea106fbcc01b6d8077d2aa6398bd4669', 'url': 'https://mtcbus.tn.gov.in/Home/routewiseinfo' }
# response = requests.get('https://api.scraperapi.com/', params = payload)
# print(response.text)



# BASE_URL = "https://mtcbus.tn.gov.in/Home/routewiseinfo"
# response = requests.get(BASE_URL)
# soup = BeautifulSoup(response.content , 'html5lib')
# prettified = soup.prettify()
# extractedBusNumbers = soup.findAll('option')
# busNumbers = []
# busInfo = {}


# for busNo in extractedBusNumbers:
#     if(busNo.text.isalnum()):
#         busNumbers.append(busNo.text)

# BUS_QUERY_URL = BASE_URL + "?csrf_test_name=d9bd9e4ea7c6a77badb564df75429950&selroute="

# for bus in busNumbers:
#     bus_info = requests.get(BUS_QUERY_URL + bus)
#     soup1 = BeautifulSoup(bus_info.content, 'html5lib')
#     route_info = soup1.find('ul',attrs={'class':'route'})
#     stops = []
#     for stop in route_info.children:
#         if(stop.text.find('\t') == 0):
#             continue
#         print(stop.text.split(" "))

# BASE_URL = "https://mtcbus.tn.gov.in/Home/fares"
# response = requests.get(BASE_URL)
# soup = BeautifulSoup(response.content , 'html5lib')
# prettified = soup.prettify()

# extractedBusServices = soup.find('ul', {'class' : 'nav nav-tabs'})
# extractedBusFares = soup.find('div' , {'class' : 'tab-content'})
# busServices = []
# faresForBusServices = dict()

# for each in extractedBusServices.children:
#     if(each.text.find('\t') == -1):
#         busServices.append(each.text)


# for i in range(len(busServices) - 1):
#     fares = extractedBusFares.find('div' , {'id' : f"tab{i}"})
#     fareList = [fare.text for fare in fares.findAll('span',{'class' :'rate'})]
#     faresForBusServices[busServices[i]] = fareList[1:len(fareList) - 1]
# l = [i for i in range(11,50,2)]
# faresForBusServices[busServices[4]] = l

# for i in busServices[:len(busServices) - 1]:
#     l = []
#     for j in faresForBusServices[i]:
#         l.append(int(j[:j.find('.')]))
#     faresForBusServices[i] = l

# print(faresForBusServices)


# API_KEY = "088393d705dabaef443fe242ea1e773a"
# RAPID_API_KEY = "be78578af0mshfcd7e082a40ac2bp1e8da6jsn1268a730bbb6"

# headers = {
#     'x-rapidapi-key': "be78578af0mshfcd7e082a40ac2bp1e8da6jsn1268a730bbb6",
#     'x-rapidapi-host': "indian-railway-irctc.p.rapidapi.com",
#     'x-rapid-api': "rapid-api-database"
# }

# LIVE_TRAIN_STATUS_URL = "https://indian-railway-irctc.p.rapidapi.com/api/trains/v1/train/status?departure_date=20250302&isH5=true&client=web&train_number=12639"



# response = requests.get(url , headers = headers )
# print(response.json())


# with open("./Backend/DataStore/TrainStations.json" , "r") as f:
#     stations = json.load(f)["stations"]

# modifiedData = dict()

# for station in stations:
#     modifiedData[station["name"]] = station["code"]


# with open("./Backend/DataStore/RailwayStations.json" , "w") as f:
#     json.dump(modifiedData , f)