#!/usr/bin/env python
# This program shows me the average scrobbles per day.
# Sure, the website tells me as well, but I want to have at least a few
# decimals, to see the changes over time.

from datetime import date, datetime
import time
from lxml import html
import requests
import re

days = [7, 30, 90, 180, 365]
d = len(days)
a = 0
# Enter your details here
username = 'StonedEars'
joined = '09/01/2009'

# Get the days between today and the lastfm joined date
date_format = "%d/%m/%Y"
date_joined = datetime.strptime(joined, date_format)
today = datetime.strptime(time.strftime("%d/%m/%Y"), date_format)
delta = today - date_joined

# get the current playcount from lastfm overall
page = requests.get('https://www.last.fm/user/' + username)
stuff = html.fromstring(page.content)
playcount = stuff.xpath('//*[@id="content"]/div[2]/header/div[2]/div/div[2]/div[2]/ul/li[1]/p/a/text()')
cleancount = int(re.sub("[^\d\.]", "", playcount[0])) / int(delta.days + 1)

# get the current playcout from the last n days
for i in range (d):
    lastpage = requests.get('https://www.last.fm/user/' + username + '/library?date_preset=LAST_' + str(days[i]) + '_DAYS')
    laststuff = html.fromstring(lastpage.content)
    lastscrob = laststuff.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul[1]/li[1]/p/text()')
    lastavg = laststuff.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul[1]/li[2]/p/text()')
    print ("Last " + str(days[i]) + " Days:")
    print ("Scrobbled Tracks: " + lastscrob[a])
    print ("Average: " + lastavg[a])
    print ("")
    a + 1

# Display the overall average
print ("Overall")
print ("Scrobbled Tracks: " + playcount[0])
print ("Passed Days: " + str(int(delta.days + 1)))
print ("Average: " + str("%.4f" % cleancount))
