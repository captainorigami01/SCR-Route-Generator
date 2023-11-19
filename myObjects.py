import random

operators = ["connect", "waterline", "airlink", "express"]

stations = [
    "Airport Terminal 1",
    "Airport Terminal 2",
    "Airport Terminal 3",
    "Airport West",
    "Angel Pass",
    "Ashlan Park",
    "Beaulieu Park",
    "Beechley",
    "Benton",
    "Benton Bridge",
    "Berrily",
    "Bodin",
    "Cambridge Street Parkway",
    "City Hospital",
    "Connolly",
    "Coxly",
    "East Berrily",
    "Eden Quay",
    "Edgemead",
    "Elsemere Junction",
    "Elsemere Pond",
    "Esterfield",
    "Faraday Road",
    "Farleigh",
    "Faymere",
    "Financial Quarter",
    "Greenslade",
    "Hampton Hargate",
    "Hemdon Park",
    "Houghton Rake",
    "James Street",
    "Leighton City",
    "Leighton Stepford Road",
    "Leighton West",
    "Llyn-By-The-Sea",
    "Millcastle",
    "Millcastle Racecourse",
    "Morganstown",
    "Morganstown Docks",
    "New Harrow",
    "Newry",
    "Newry Harbour",
    "Northshore",
    "Port Benton",
    "Rocket Parade",
    "Rosedale Village",
    "St Helens Bridge",
    "Starryloch",
    "Stepford Airport Parkway",
    "Stepford Airport Central",
    "Stepford Central",
    "Stepford East",
    "Stepford High Street",
    "Stepford United Football Club",
    "Stepford Victoria",
    "Upper Staploe",
    "Water Newton",
    "West Benton",
    "Westercoast",
    "Westwyvern",
    "Whitefield",
    "Whitefield Lido",
    "Whitney Green",
    "Willowfield",
    "Woodhead Lane"
]


class Randomiser:
    def __init__(self, start: str = ""):
        self.start = start
        if self.start == "":
            self.end = self.start = stations[random.randint(0, len(stations)-1)]
        self.getRouteUpdate()

    def getRoute(self):
        return self.start, self.end

    def setStart(self, start):
        self.start = start
        self.getRouteUpdate()

    def getRouteUpdate(self):
        end = self.start
        while end == self.start:
            end = stations[random.randint(0, len(stations)-1)]
        self.end = end


