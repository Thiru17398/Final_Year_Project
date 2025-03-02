from playwright.sync_api import sync_playwright
import json


class LocalTrainManager:

    stations = []
    source = ""
    destination = ""

    def __init__(self):
        with open("./DataStore/RailwayStations.json" , "r") as f:
            self.stations = json.load(f)
        
    def getTrainsBetweenStations(self , source , destination):
        self.source = source
        self.destination = destination
    
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://enquiry.indianrail.gov.in/mntes/q?opt=MainMenu&subOpt=tbs&excpType=")
            page.click("#sidebar > form > ul > li:nth-child(4) > a")
            source = source.upper()
            destination = destination.upper()
            page.wait_for_selector("#jFromStationInput" , timeout = 60000)
            with open("./DataStore/RailwayStations.json" , "r") as f:
                data = json.load(f)
            
            page.fill("#jFromStationInput" , source + " - " + data[source])
            page.fill("#jToStationInput" , destination + " - " + data[destination])
            page.click("#content > form:nth-child(3) > div:nth-child(4) > div:nth-child(2) > div > input.btn.btn-primary")
            page.wait_for_selector("#myTable", timeout = 60000)
            table = page.query_selector("#myTable")
            noOfTrains = int(page.query_selector("#myTable > thead > tr > th > font").inner_text().split(" ")[0])


            train_details = []

            for i in range(1 , noOfTrains + 1):
                train = page.query_selector(f"#myTable > tbody > tr:nth-child({i}) > td")
                train_details.append({
                    "trainNumber" : train.query_selector("span:nth-child(1) > b").inner_text(),
                    "departureTime" : train.query_selector("div:nth-child(5) > span:nth-child(1) > b").inner_text(),
                    "arrivalTime" : train.query_selector("div:nth-child(5) > span.float-right > b").inner_text(),
                    "journeyDuration" : self.getDuration(train.query_selector("div:nth-child(5) > div").inner_text()[2:7])
                })
        
        return train_details
    
    def getDuration(self, duration):
        res = ""
        hours , minutes = map(int , duration.split(":"))
        if(hours > 0):
            res += str(hours) + " hour "
        res += str(minutes) + " minutes."


