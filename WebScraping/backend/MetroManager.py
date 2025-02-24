
import json


class MetroManager:

    metro_details = None
    source = dict()
    destination = dict()

    exchange_indices = [
        {
        "blue_line_indices ": [15 , 22],
        "green_line_indices" : [1 , 15] 
        }
    ]

    def __init__(self):
        with open('./DataStore/MetroInfo.json', 'r') as file:
            self.metro_details = json.load(file)
    

    def getMetroRoute(self, source, destination):
        self.source , self.destination = self.getSourceAndDestination(source ,destination)
        blue_line = self.metro_details['blue_line_stations']
        green_line = self.metro_details['green_line_stations']
        end_point_stations = self.metro_details['end_point_stations']

        blue_line_indices = [blue_line.index(self.source) if self.source in blue_line else -1 , blue_line.index(self.destination) if self.destination in blue_line else -1]
        green_line_indices = [green_line.index(self.source) if self.source in green_line else -1 , green_line.index(self.destination) if self.destination in green_line else -1]

        if(blue_line_indices[0] != -1 and blue_line_indices[1] != -1):
            return end_point_stations['blue_line']['forward'] if blue_line_indices[0] < blue_line_indices[1] else end_point_stations['blue_line']['backward']
        elif(green_line_indices[0] != -1 and green_line_indices[1] != -1):
            return end_point_stations['green_line']['forward'] if green_line_indices[0] < green_line_indices[1] else end_point_stations['green_line']['backward']

    
    def getMetroFare(self , source , destination):
        
        
        fare = self.getFare(abs(self.source['distance'] - self.destination['distance']))

        return fare

    
    def getFare(self , distance):
        if(distance > 0 and distance <= 2):
            return 10
        elif(distance > 2 and distance <= 5):
            return 20
        elif(distance > 5 and distance <= 12):
            return 30
        elif(distance > 12 and distance <= 21):
            return 40
        else:
            return 50
    
    def getSourceAndDestination(self, source, destination):
        sour = None
        dest = None
        for station in self.metro_details['blue_line_stations']:
            if station['station'].lower() == source:
                sour = station
            if station['station'].lower() == destination:
                dest = station
        for station in self.metro_details['green_line_stations']:
            if station['station'].lower() == source:
                sour = station
            if station['station'].lower() == destination:
                dest = station
        
        return sour , dest
