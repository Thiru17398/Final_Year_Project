import requests
from bs4 import BeautifulSoup

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
    
    
    

