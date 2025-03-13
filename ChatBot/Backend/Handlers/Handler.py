import random
import sys
import os
import json
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from WebScraping.backend.BusManager import BusManager
from WebScraping.backend.MetroManager import MetroManager
from WebScraping.backend.LocalTrainManager import LocalTrainManager

class Handler:
    busManager = None
    metroManager = None
    localTrainManager = None


    def __init__(self):
        self.busManager = BusManager()
        self.metroManager = MetroManager()
        self.localTrainManager = LocalTrainManager()
    
    def getBuses(self , source , destination , response):
        buses = self.busManager.getBuses(source , destination)
        return response.format(source = source.upper() , destination = destination.upper() , bus_routes = "\n ".join(buses.keys())).replace("\n" , "\n")

    def getBusFare(self, source , destination , response):
        fare = self.busManager.getBusFare(source , destination)
        fare_list = ""
        for service in fare:
            fare_list += service + " : \u20B9" + str(fare[service]) +  "\n"

        return response.format(source = source , destination = destination , fare_list = fare_list).replace("\n" , "\n")


    def getMetroFare(self , source , destination , response):
        metroFare = self.metroManager.getMetroFare(source , destination)
        return response.format(source = source , destination = destination , fare = metroFare , code = '\u20B9').replace("\n","\n")

    def getMetroTimings(self , source , destination , response):
        metroTimings = self.metroManager.getMetroTimings(source , destination)
        return response.format(source = source , destination = destination , timings = " ".join(metroTimings))

    def getMetroRoutePlanning(self , source , destination , responses):
        metro_route , exchange_station , distance = self.metroManager.getMetroRoute(source , destination)

        if(len(metro_route) == 2):
            return responses[2].format(source = source , destination = destination , endPoint1 = metro_route[0] , endPoint2 = metro_route[1] , exchangeStation = exchange_station , distance = distance).replace("\n" , "\n")
        else:
            return random.choice(responses[:2]).format(source = source , destination = destination , endPoint = metro_route , distance = distance).replace("\n" , "\n")

    async def getLocalTrainBetweenStations(self , source , destination , response):
        trains = await self.localTrainManager.getTrainsBetweenStations(source , destination)
        trains_info = ""
        now = datetime.now().strftime("%H:%M:%S")
        i = 1
        for train in trains:
            if(i == 5):
                break
            dept = train["departureTime"]
            if(self.validateDeparture(now , dept)):
                trains_info += str(i) + ". **" + train["departureTime"] + "** From **" + source.upper() + "** and  will reach **" + destination.upper() + "** by **" + train["arrivalTime"] + "** \n"
                i+=1
        return response.format(source = source.upper() , destination = destination.upper() , train_info = trains_info).replace("\n","\n")
    

    def validateDeparture(self , now , dept):
        h1 , m1 = map(int , dept.split(":"))
        h2 , m2 , s1 = map(int , now.split(":"))
        if(h1 == h2):
            return m1 >= m2
        return h1 > h2

