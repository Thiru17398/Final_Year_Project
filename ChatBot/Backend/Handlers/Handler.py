
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from WebScraping.backend.BusManager import BusManager
from WebScraping.backend.MetroManager import MetroManager

class Handler:
    busManager = None
    metroManager = None
    suburbanTrainManager = None
    source = None
    destination = None


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

        