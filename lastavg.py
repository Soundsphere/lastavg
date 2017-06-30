#!/usr/bin/env python
# This program shows me the average scrobbles per day.
# Sure, the website tells me as well, but I want to have at least a few
# decimals, to see the changes over time. It also displays the average scrobbles
# and artists for the last 7, 30, 90, 180 and 365 on one page

from datetime import date, datetime
import time
from lxml import html
import requests
import re

# set a few things like days and the integer for the for loop
days = 7, 30, 90, 180, 365
d = len(days)

# Enter your details here. Date format is DD/MM/YYYY
username = 'StonedEars'
joined = '09/01/2009'

# Get the days between today and the lastfm joined date
def date():
    date_format = "%d/%m/%Y"
    date_joined = datetime.strptime(joined, date_format)
    today = datetime.strptime(time.strftime("%d/%m/%Y"), date_format)
    delta = today - date_joined
    return delta.days

# Print some sort of header
print("Stats for " + username + ":\n")

# This for-loop iterates 5 times to get the average, the playcount and the scrobbled artists for each number of days
# stored in the days list and displays the output
for i in range (d):
    lastpage_scrobbles = requests.get('https://www.last.fm/user/' + username + '/library?date_preset=LAST_' + str(days[i]) + '_DAYS')
    lastpage_artists = requests.get('https://www.last.fm/user/' + username + '/library/artists?date_preset=LAST_' + str(days[i]) + '_DAYS')
    laststuff_scrobbles = html.fromstring(lastpage_scrobbles.content)
    laststuff_artists = html.fromstring(lastpage_artists.content)
    lastpage_scrobbles = laststuff_scrobbles.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul[1]/li[1]/p/text()')
    lastpage_artists = laststuff_artists.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul/li/p/text()')
    lastavg = laststuff_scrobbles.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul[1]/li[2]/p/text()')
    # print the results from the website
    print ("Last " + str(days[i]) + " Days:")
    print ("Scrobbled Artists: " + lastpage_artists[0])
    print ("Scrobbled Tracks: " + lastpage_scrobbles[0])
    print ("Average: " + lastavg[0] + "\n")

# get the current playcount from lastfm overall
def scrobbles():
    page_scrobbles = requests.get('https://www.last.fm/user/' + username)
    stuff = html.fromstring(page_scrobbles.content)
    page_scrobbles = stuff.xpath('//*[@id="content"]/div[2]/header/div[2]/div/div[2]/div[2]/ul/li[1]/p/a/text()')
    return page_scrobbles[0]

# get the clean average of scrobbles
def cleanavg():
    cleancount = int(re.sub("[^\d\.]", "", scrobbles())) / int(date() + 1)
    return cleancount

# get the current amount of different artists scrobbled from lastfm overall
def artists():
    page_artists = requests.get('https://www.last.fm/user/' + username + '/library/artists')
    stuff_artists = html.fromstring(page_artists.content)
    artists = stuff_artists.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul/li/p/text()')
    return artists[0]

# Display the overall average
print ("Overall:")
print ("Scrobbled Artists: " + artists())
print ("Scrobbled Tracks: " + scrobbles())
print ("Passed Days: " + str(int(date() + 1)))
print ("Average: " + str("%.4f" % cleanavg()))
