import json
import os



class BusManager:
    busInfo = {}
    busServices = ['Ordinary Services', 'Express Services', 'Deluxe Services', 'A/C Service', 'Night services']
    busFares = {'Ordinary Services': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23, 24, 24], 
                'Express Services': [7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 22, 24, 24, 25, 25, 27, 27, 28, 28, 30, 30, 31, 31, 33, 33, 34, 34, 35, 35], 
                'Deluxe Services': [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 31, 33, 33, 35, 35, 37, 37, 39, 39, 41, 41, 43, 43, 45, 45, 47, 47, 49, 49], 
                'A/C Service': [15, 15, 20, 20, 20, 30, 30, 30, 40, 40, 40, 40, 40, 40, 50, 50, 50, 50, 60, 60, 60, 60, 60, 70, 70, 70, 70, 80, 80, 80], 
                'Night services': [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]}
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

    def getBusFare(self, source , destination):
        buses = self.getBuses(source , destination)
        faresForBuses = dict()
        for bus in buses:
            noOfStops = len(self.getInbetweenStops(bus)) - 2
            for service in self.busFares:
                faresForBuses[service] = self.busFares[service][noOfStops - 1]
        return faresForBuses

