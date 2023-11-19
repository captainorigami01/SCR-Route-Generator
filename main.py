import json
import urllib
import myObjects
import time
import verifyJson
import random
import os
import webbrowser

# update checker

VERSION = "0.1"


verifyJson.checkroutes()
verifyJson.checktrains()

trainList = []
routeList = []

myTimetable = {

}

with open("trains.json", "r") as f:
    trains = json.loads(f.read())
    for train in trains:
        trainList.append(train)

with open("routes.json", "r") as f:
    routes = json.loads(f.read())
    for route in routes:
        routeList.append(route)


inp = "NO"

inp2 = "NO"

while inp2 not in ["1", "2"]:
    inp2 = str(input(f"Select option:\n[1] Driver Timetable\n[2] Passenger"))


if inp2 == "1":
    print("Please ensure all owned routes and trains are entered into the ownedRoutesTrains.json file")
    with open("ownedRoutesTrains.json", "r") as f:
        owned = json.loads(f.read())
        ownedTrains = owned["trains"]["owned"]
        ownedRoutes = owned["routes"]["owned"]
        ownedOperators = owned["operators"]["owned"]

    for operator in ownedOperators:
        if operator not in myObjects.operators:
            print(f"Owned Operator not found: {operator}")
            input()
            exit()

    for train in ownedTrains:
        if train not in trainList:
            print(f"Owned train not found: {train}")
            input()
            exit()

    selectedOperator = ownedOperators[random.randint(0, len(ownedOperators)-1)]
    endOfRoute = None
    selectedTrain = None
    selectedTrainOperator = None
    nextRoute = None

    while selectedTrain is None or selectedTrainOperator != selectedOperator:
        selectedTrain = ownedTrains[random.randint(0, len(ownedTrains)-1)]
        selectedTrainOperator = trains[selectedTrain]["operator"]
    print(selectedTrain)
    for x in range(0, random.randint(4, 15)):
        currentOperator = ""
        while currentOperator != selectedOperator:
            routeSelected = ownedRoutes[random.randint(0, len(ownedRoutes)-1)]
            if nextRoute is not None:
                routeSelected = nextRoute
                nextRoute = None
            for route in routes:
                if route == routeSelected:
                    if routes[route]["operator"] == selectedOperator:
                        routeTrains = routes[route]["trains"]
                        trainAllowed = False
                        if "A" in routeTrains:
                            if "-" + selectedTrain in routeTrains:
                                trainAllowed = False
                            else:
                                trainAllowed = True
                        elif selectedTrain in routeTrains:
                            trainAllowed = True
                        else:
                            trainAllowed = False
                        routeValid = False
                        idx = 0
                        start = ""
                        stop = ""
                        stops = routes[route]["stops"]
                        if endOfRoute is None:
                            print("Start of WTT")
                            start = stops[0]
                            stop = stops[len(stops)-1]
                            idx = 0
                            routeValid = True
                        elif endOfRoute == stops[0]:
                            print("start from 0")
                            start = endOfRoute
                            stop = stops[len(stops)-1]
                            idx = 0
                            routeValid = True
                        elif endOfRoute == stops[len(stops)-1]:
                            print("Start from end")
                            start = endOfRoute
                            stop = stops[0]
                            idx = len(stops)-1
                            routeValid = True
                        else:
                            print(f"Route {route} doesn't work in current timetable")

                        if routeValid and trainAllowed:
                            currentOperator = routes[route]["operator"]
                            endOfRoute = stop
                            myTimetable[x] = {"route": route, "index": idx, "start": start, "end": stop}
                            if routes[route]["operator"] == "express" and endOfRoute == "Benton":
                                nextRoute = route
    # print(myTimetable)
    outputHtml = f"<!DOCTYPE html><html><head><title>SCR Working Time Table</title>"
    outputHtml += f"<link rel='stylesheet' type='text/css' href='style.css'</head><body>"
    outputHtml += "<h1>SCR Working Time Table</h1>\n"
    outputHtml += f"<blockquote>Selected train: Class {selectedTrain} with {selectedOperator}</blockquote>\n"
    for wtt in myTimetable:
        timetable = myTimetable[wtt]["route"]
        index = myTimetable[wtt]["index"]
        start = myTimetable[wtt]["start"]
        end = myTimetable[wtt]["end"]
        duration = routes[timetable]["duration"]
        stops = routes[timetable]["stops"]
        outputHtml += f"<details><summary>{timetable}: {start} - {end}, {duration} minutes</summary>Calling at: "
        if index > 0:

            for i in range(len(stops)-1, -1, -1):
                if (timetable == "R060" and stops[i] in ["Airport Terminal 1", "Airport Terminal 3"]) or (stops[i] in ["Berrily", "Airport Terminal 1"]):
                    pass
                else:
                    outputHtml += stops[i]
                    if i > 0:
                        outputHtml += ", "
        else:
            for i in range(0, len(stops)):
                outputHtml += stops[i]
                if i < len(stops)-1:
                    outputHtml += ", "
        outputHtml += "</details>"
    outputHtml += f"<footer>&copy; Copyright Archie Harrison 2023</footer></body></html>"
    with open("wtt.html", 'w') as f:
        f.write(outputHtml)

    fn = f"file:///{os.getcwd()}/wtt.html"
    webbrowser.open_new_tab(fn)

if inp2 == "2":

    while inp not in myObjects.stations and inp != "":
        inp = str(input("Enter start location or leave blank for random start: \n"))

    v1, v2 = myObjects.Randomiser(start=inp).getRoute()

    print(f"Start: {v1}\nEnd: {v2}")
    input("Press enter to start stopwatch")
    startTime = time.time()
    input("Press enter to stop timer")
    elapsed = time.time() - startTime
    print(f"Time elapsed: {elapsed}s")
    input()