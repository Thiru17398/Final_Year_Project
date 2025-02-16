import requests
from bs4 import BeautifulSoup
import json


# payload = { 'api_key': 'ea106fbcc01b6d8077d2aa6398bd4669', 'url': 'https://mtcbus.tn.gov.in/Home/routewiseinfo' }
# response = requests.get('https://api.scraperapi.com/', params = payload)
# print(response.text)



BASE_URL = "https://mtcbus.tn.gov.in/Home/routewiseinfo"

response = requests.get(BASE_URL)


soup = BeautifulSoup(response.content , 'html5lib')

prettified = soup.prettify()

extractedBusNumbers = soup.findAll('option')

busNumbers = []

busInfo = {}


for busNo in extractedBusNumbers:
    if(busNo.text.isalnum()):
        busNumbers.append(busNo.text)

BUS_QUERY_URL = BASE_URL + "?csrf_test_name=d9bd9e4ea7c6a77badb564df75429950&selroute="

for bus in busNumbers:
    bus_info = requests.get(BUS_QUERY_URL + bus)
    soup1 = BeautifulSoup(bus_info.content, 'html5lib')
    route_info = soup1.find('ul',attrs={'class':'route'})
    stops = []
    for stop in route_info.children:
        if(stop.text.find('\t') == 0):
            continue
        print(stop.text.split(" "))

obj = json.dumps(busInfo)
with open('busInfo.json', 'w') as outfile:
    outfile.write(obj)

resJson = dict()
with open('busInfo.json' , 'r') as f:
  data = json.load(f)
  for bus in data:
    resJson[bus] = {
        'stops' : data[bus]
    }

with open('busInfo.json' , 'w') as f:
  json.dump(resJson , f)

all_stops = set()

stop_wise_bus = dict()

for bus in busInfo:
  for stop in busInfo[bus]:
    if stop not in stop_wise_bus:
      stop_wise_bus[stop] = [bus]
    else:
      stop_wise_bus[stop].append(bus)

with open('stop_wise_bus.json' , 'w') as f:
  json.dump(stop_wise_bus , f)

METRO_URL = "https://chennaimetrorail.org/"

response = requests.get(METRO_URL)
soup = BeautifulSoup(response.content , 'html5lib')

metro_stations = soup.find_all('div' , attrs= {'class' : 'by-br'}) 

metro_stations_names = []
for station in metro_stations:
  metro_stations_names.append(station.text.strip())

blue_line_stations = ['Wimco Nagar Depot Metro', 'Wimco Nagar Metro', 'Thiruvotriyur Metro', 'Thiruvottriyur Theradi Metro', 'Kaladipet Metro', 'Tollgate Metro', 'New Washermenpet Metro', 'Tondiarpet Metro', 'Sir Thiyagaraya College Metro', 'Washermenpet Metro', 'Mannadi', 'Highcourt', 'Puratchi Thalaivar Dr. M.G.Ramachandran Central Metro', 'Government Estate', 'LIC', 'Thousand Lights', 'AG – DMS', 'Teynampet', 'Nandanam', 'Saidapet Metro', 'Little Mount', 'Guindy', 'Arignar Anna Alandur Metro', 'OTA-Nanganallur Road', 'Meenambakkam', 'Chennai International Airport']
green_line_station = ['Puratchi Thalaivar Dr. M.G.Ramachandran Central Metro', 'Egmore Metro', 'Nehru Park', 'Kilpauk', 'Pachaiyappa’s College', 'Shenoy Nagar', 'Anna Nagar East', 'Anna Nagar Tower', 'Thirumangalam', 'Koyambedu', 'Puratchi Thalaivi Dr.J.Jayalalithaa CMBT Metro', 'Arumbakkam', 'Vadapalani', 'Ashok Nagar', 'Ekkattuthangal', 'Arignar Anna Alandur Metro', 'St. Thomas Mount Metro']

exchange_stations = ['Puratchi Thalaivar Dr. M.G.Ramachandran Central Metro', 'Arignar Anna Alandur Metro']

