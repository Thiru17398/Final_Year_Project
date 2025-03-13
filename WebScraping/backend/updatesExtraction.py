import requests
import json
from bs4 import BeautifulSoup


bus_announcements_url = "https://mtcbus.tn.gov.in/Home/news"

response = requests.get(bus_announcements_url)

soup = BeautifulSoup(response.content , 'html5lib')

prettified = soup.prettify()

announcements = soup.find_all("div" , {'class' : 'col-sm-12'})

print(announcements)