#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests
import pprint

# Get loved tracks
lovedUrl = "http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=StonedEars&api_key=269eeebb75b0c41507ec4601f66f92c9&format=json"
loved = requests.get(lovedUrl)
loved.raise_for_status()

# Load JSON data into a Python variable.
lovedData = json.loads(loved.text)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(lovedData)
