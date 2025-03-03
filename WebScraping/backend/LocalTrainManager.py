from playwright.async_api import async_playwright
import json
import asyncio


class LocalTrainManager:

    stations = []
    source = ""
    destination = ""

    def __init__(self):
        with open("./DataStore/RailwayStations.json" , "r") as f:
            self.stations = json.load(f)
        
    async def getTrainsBetweenStations(self , source , destination):
        self.source = source
        self.destination = destination
    
        async with async_playwright() as p:
            
            browser = await p.chromium.launch(headless=False)
            context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" , java_script_enabled=True)
            page = await context.new_page()

            await page.add_init_script("""Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""")
            
            input("enter")
            await page.goto("https://enquiry.indianrail.gov.in/mntes/" , wait_until="domcontentloaded")
            await page.screenshot(path="captcha.png")
            await page.click("#sidebar > form > ul > li:nth-child(4) > a")
            
            source = source.upper()
            destination = destination.upper()
            await page.wait_for_selector("#jFromStationInput" , timeout = 60000)
            with open("./DataStore/RailwayStations.json" , "r") as f:
                data = json.load(f)
            
            await page.fill("#jFromStationInput" , source + " - " + data[source])
            await page.fill("#jToStationInput" , destination + " - " + data[destination])
            await page.click("#content > form:nth-child(3) > div:nth-child(4) > div:nth-child(2) > div > input.btn.btn-primary")
            await page.wait_for_selector("#myTable", timeout = 60000)
            await page.wait_for_timeout(3000)
            response = await page.query_selector("#myTable > thead > tr > th > font")
            noOfTrains = 0
            if response:
                text = await response.inner_text()
                noOfTrains = int(text.split(" ")[0])
                


            train_details = []

            for i in range(1 , noOfTrains + 1):
                train = await page.query_selector(f"#myTable > tbody > tr:nth-child({i}) > td")
                trainNumber = await train.query_selector("span:nth-child(1) > b")
                departureTime = await train.query_selector("div:nth-child(5) > span:nth-child(1) > b")
                arrivalTime = await train.query_selector("div:nth-child(5) > span.float-right > b")
                journeyDuration = await train.query_selector("div:nth-child(5) > div")
                if journeyDuration:
                    journeyDuration = await journeyDuration.inner_text()
                    journeyDuration = self.getDuration(journeyDuration[2:7])
                                                         
                train_details.append({
                        "trainNumber" : await trainNumber.inner_text(),
                        "departureTime" : await departureTime.inner_text(),
                        "arrivalTime" : await arrivalTime.inner_text(),
                        "journeyDuration" : journeyDuration
                        })
        
        return train_details
    
    def getDuration(self, duration):
        res = ""
        hours , minutes = map(int , duration.split(":"))
        if(hours > 0):
            res += str(hours) + " hour "
        res += str(minutes) + " minutes."


