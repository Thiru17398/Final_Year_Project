import json
import os



class BusManager:
    busInfo = {}
    origin = None
    destination = None
    def __init__(self):
        result = {}
        with open('./DataStore/busInfo.json','r') as f:
            result = json.load(f)
        self.busInfo = result
    

    def getData(self):
        return self.busInfo
    
    def getBuses(self , origin , destination):
        stop_wise_bus = []

        self.origin = origin.upper()
        self.destination = destination.upper()

        with open('./DataStore/StopWiseBusInfo.json') as f:
            stop_wise_bus = json.load(f)

        origin_stopping_buses = stop_wise_bus[self.origin]
        destination_stopping_buses = stop_wise_bus[self.destination]

        bus_confirmation = dict()

        for bus in origin_stopping_buses:
            if bus not in bus_confirmation:
                bus_confirmation[bus] = 0
            bus_confirmation[bus] += 1

        for bus in destination_stopping_buses:
            if bus not in bus_confirmation:
                bus_confirmation[bus] = 0
            bus_confirmation[bus] -= 1

        buses_between_the_routes = dict()

        for bus in bus_confirmation:
            if bus_confirmation[bus] == 0:
                buses_between_the_routes[bus] = self.getInbetweenStops(bus)

        return buses_between_the_routes
    
    def getAllStops(self):
        with open('./DataStore/StopWiseBusInfo.json') as f:
            stop_wise_bus = json.load(f)
        stop_wise_bus = list(stop_wise_bus.keys())
        stop_wise_bus.sort()
        return stop_wise_bus

    def getInbetweenStops(self , busNo):
        route = self.busInfo[busNo]['stops']

        start = route.index(self.origin)
        end = route.index(self.destination)

        result = route[start : end + 1]
        if start > end:
            result = route[end : start + 1][::-1]
        return result
