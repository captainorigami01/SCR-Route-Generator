import json
import myObjects


def checktrains():
    with open("trains.json", "r") as f:
        trains = json.loads(f.read())

    for train in trains:
        try:
            if trains[train]["operator"] not in myObjects.operators:
                print(f"Operator not found for class {train} with operator: {trains[train['operator']]}")
                exit()
            op = trains[train]["operator"]
            length = trains[train]["length"]
        except KeyError as err:
            print(f"{err} not found for train {train}")
            input()
            exit()

    print("trains file OK")


def checkroutes():
    with open("routes.json", "r") as f:
        routes = json.loads(f.read())

    for route in routes:
        trainsAllowed = ""
        try:
            for train in routes[route]["trains"]:
                if train == "A":
                    trainsAllowed = "All Trains allowed except the following: " + trainsAllowed
                elif str(train).__contains__("-"):
                    myTrain = str(train).replace("-", "")
                    trainsAllowed += "No Class " + myTrain + " "
                else:
                    trainsAllowed += f"Class {train} "
            duration = routes[route]["duration"]

            for station in routes[route]["stops"]:
                if station not in myObjects.stations:
                    print(f"Station not found on route: {route}, with station: {station}")
                    input()
                    exit()

            op = routes[route]["operator"]
            if op not in myObjects.operators:
                print(f"Operator not found on route: {route}, with operator: {op}")
        except KeyError as err:
            print(f"{err} not found for route {route}")
            input()
            exit()

    print("routes file verified")

