
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from WebScraping.backend.BusManager import BusManager 

class BusHandler:
    busManager = None
    source = None
    destination = None


    def __init__(self):
        self.busManager = BusManager()
    
    def getBuses(self , source , destination , response):
        buses = self.busManager.getBuses(source , destination)
        if("stops" in response.lower()):
            result = []
            if(len(buses.keys()) > 0):
                for bus in buses:
                    result.append(response.format(noOfStops = len(buses[bus]) , source = source , destination = destination , busNumber = bus , allStops = "->".join(buses[bus])))
            else:
                result.append("No buses found between {source} to {destination}")
            return "\n".join(result)
        if("bus" in response.lower()):
            return response.format(source = source , destination = destination , suggested_buses = " ".join(buses.keys()))

        