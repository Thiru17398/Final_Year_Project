import requests
from bs4 import BeautifulSoup

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



    
    
    

