#! python3

import json, requests
import pprint

# Get user info
info = requests.get("http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=StonedEars&api_key=269eeebb75b0c41507ec4601f66f92c9&format=json")
info.raise_for_status()

# Load JSON data into a Python variable.
infoData = json.loads(info.text)

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(infoData)

pc = infoData["user"]
print(pc["playcount"])
