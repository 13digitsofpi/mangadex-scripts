#!/usr/bin/env python3
from time import gmtime, strftime
import json

# Saves, adds and checks date. Meant to reduce requests made to mangadex. TODO Implement 

# Appends a date key to end of file
def writedate(jsonfile):
    with open(jsonfile, "r") as f:
        wdt = json.load(f)
    cdate = strftime("%j", gmtime())
    wdt["date"] = cdate
    with open(jsonfile, "w") as f:
        json.dump(wdt, f, indent=2)

# writes the json to a file
def writejson(jsonfile, towrite):
    data = json.loads(towrite)
    with open(jsonfile, "w") as f:
        json.dump(data, f, indent=2)
        
# Checks if date is in a week
def checkdate(jsonfile):
    with open(jsonfile, "r") as f:
        jfile = json.load(f)
    filedate = int(jfile["date"])
    cdate = int(strftime("%j", gmtime()))
    if cdate in range(filedate, filedate) + 7)):
        print("old")
