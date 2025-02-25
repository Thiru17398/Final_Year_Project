
import json
import random


class MetroManager:

    metro_details = None
    source = dict()
    destination = dict()

    exchange_indices = [
        {
        "blue_line_indices ": [15 , 22],
        "green_line_indices" : [0 , 15] 
        }
    ]

    def __init__(self):
        with open('./DataStore/MetroInfo.json', 'r') as file:
            self.metro_details = json.load(file)


    

    def getMetroRoute(self, source, destination):
        self.source , self.destination = self.getSourceAndDestination(source ,destination)
        blue_line = self.metro_details['blue_line_stations']
        green_line = self.metro_details['green_line_stations_st_thomas_mount']
        exchane_station = None

        distance = "%.2f"%(abs(self.source['distance'] - self.destination['distance']))
        print(distance)
        end_point_stations = self.metro_details['end_point_stations']

        blue_line_indices = [blue_line.index(self.source) if self.source in blue_line else -1 , blue_line.index(self.destination) if self.destination in blue_line else -1]
        green_line_indices = [green_line.index(self.source) if self.source in green_line else -1 , green_line.index(self.destination) if self.destination in green_line else -1]
        if(green_line_indices[0] != -1 and destination == 'airport'):
            green_line_indices[1] = 16
        
        

        if(blue_line_indices[0] != -1 and blue_line_indices[1] != -1):
            return self.getEndpointMetro(blue_line_indices , end_point_stations , 'blue_line') , None , distance
        elif(green_line_indices[0] != -1 and green_line_indices[1] != -1):
            end_station = self.getEndpointMetro(green_line_indices , end_point_stations , 'green_line')
            if(len(end_station) == 2):
                return end_station[1] if destination == 'airport' else end_station[0] , None , distance
            else:
                return end_station , None , distance
        elif(blue_line_indices[0] != -1 and green_line_indices[1] != -1):
            metro_to_be_taken = []
            stops_between = [-1 , -1]
            stops_between[0] = (blue_line_indices[0] - 15) + green_line_indices[1]
            stops_between[1] = (22 - blue_line_indices[0]) + (15 - green_line_indices[1])

            if(blue_line_indices[0] < 15):
                metro_to_be_taken.append(end_point_stations['blue_line']['forward'])
                exchane_station = self.metro_details['exchange_stations'][0]
                metro_to_be_taken.append(end_point_stations['green_line']['forward'][0])
            elif(stops_between[0] < stops_between[1]):
                metro_to_be_taken.append(end_point_stations['blue_line']['backward'])
                exchane_station = self.metro_details['exchange_stations'][0]
                metro_to_be_taken.append(end_point_stations['green_line']['forward'][0])
            else:
                metro_to_be_taken.append(end_point_stations['blue_line']['forward'])
                exchane_station = self.metro_details['exchange_stations'][1]
                metro_to_be_taken.append(end_point_stations['green_line']['backward'])
            
            return metro_to_be_taken , exchane_station , distance
        else:
            metro_to_be_taken = []
            stops_between = [-1 , -1]
            stops_between[0] = (green_line_indices[0]) + (blue_line_indices[1] - 15)
            stops_between[1] = (15 - green_line_indices[0]) + (22 - blue_line_indices[1])

            if(blue_line_indices[1] < 15):
                metro_to_be_taken.append(end_point_stations['green_line']['backward'])
                exchane_station = self.metro_details['exchange_stations'][0]
                metro_to_be_taken.append(end_point_stations['blue_line']['backward'])
            elif(stops_between[0] < stops_between[1]):
                metro_to_be_taken.append(end_point_stations['green_line']['backward'])
                exchane_station = self.metro_details['exchange_stations'][0]
                metro_to_be_taken.append(end_point_stations['blue_line']['forward'])
            else:
                metro_to_be_taken.append(end_point_stations['green_line']['forward'][0])
                exchane_station = self.metro_details['exchange_stations'][1]
                metro_to_be_taken.append(end_point_stations['blue_line']['backward'])
            
            return metro_to_be_taken , exchane_station , distance
            


    def getEndpointMetro(self , indices , end_point_stations , line):
        return end_point_stations[line]['forward'] if indices[0] < indices[1] else end_point_stations[line]['backward']


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
        for station in self.metro_details['green_line_stations_st_thomas_mount']:
            if station['station'].lower() == source:
                sour = station
            if station['station'].lower() == destination:
                dest = station
        dest = self.metro_details['green_line_stations_airport'][-1] if destination == 'airport' else dest 
        
        return sour , dest
