import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from WebScraping.backend.BusManager import BusManager
from WebScraping.backend.MetroManager import MetroManager

class Handler:
    busManager = None
    metroManager = None
    suburbanTrainManager = None


    def __init__(self):
        self.busManager = BusManager()
        self.metroManager = MetroManager()
    
    def getBuses(self , source , destination , response):
        buses = self.busManager.getBuses(source , destination)
        return response.format(source = source , destination = destination , bus_routes = " ".join(buses.keys()))

    def getMetroFare(self , source , destination , response):
        metroFare = self.metroManager.getMetroFare(source , destination)
        return response.format(source = source , destination = destination , fare = metroFare , code = '\u20B9')

    def getMetroTimings(self , source , destination , response):
        metroTimings = self.metroManager.getMetroTimings(source , destination)
        return response.format(source = source , destination = destination , timings = " ".join(metroTimings))

    def getMetroRoutePlanning(self , source , destination , responses):
        metro_route , exchange_station , distance = self.metroManager.getMetroRoute(source , destination)

        if(len(metro_route) == 2):
            return responses[2].format(source = source , destination = destination , endPoint1 = metro_route[0] , endPoint2 = metro_route[1] , exchangeStation = exchange_station , distance = distance)
        else:
            return random.choice(responses[:2]).format(source = source , destination = destination , endPoint = metro_route , distance = distance)

        