#!/usr/bin/env python
# Shows all scrobbling info for the last 7, 30, 90, 180, 360 days as well as
# the scrobbled artist for that timeframe along with the average scrobbles

from datetime import datetime
import time
import re
import requests
from lxml import html

# set a few things like days and the integer for the for loop
DAYS = 7, 30, 90, 180, 365
D = len(DAYS)

# Enter your details here. Date format is DD/MM/YYYY
USERNAME = 'StonedEars'
JOINED = '09/01/2009'
BASE = 'https://www.last.fm/user/'

# Get the days between today and the lastfm JOINED date
def joineddate():
    """
    Return the days on last.fm.

    Takes the JOINED constant and calculates the days on lastm.
    """

    date_format = "%d/%m/%Y"
    date_joined = datetime.strptime(JOINED, date_format)
    today = datetime.strptime(time.strftime("%d/%m/%Y"), date_format)
    delta = today - date_joined
    return delta.days

def main():
    # Print some sort of header
    print("Stats for " + USERNAME + ":\n")

    # This for-loop iterates 5 times to get the average, the playcount and the scrobbled artists for
    # each number of days stored in the days tuple and displays the output
    try:
        for i in range(D):
            lastpage_scrobbles = requests.get( BASE + USERNAME + '/library?date_preset=LAST_' + str(DAYS[i]) + '_DAYS')
            lastpage_artists = requests.get( BASE + USERNAME + '/library/artists?date_preset=LAST_' + str(DAYS[i]) + '_DAYS')
            laststuff_scrobbles = html.fromstring(lastpage_scrobbles.content)
            laststuff_artists = html.fromstring(lastpage_artists.content)
            lastpage_scrobbles = laststuff_scrobbles.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul[1]/li[1]/p/text()')
            lastpage_artists = laststuff_artists.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul/li/p/text()')
            lastavg = laststuff_scrobbles.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul[1]/li[2]/p/text()')
            print("Last " + str(DAYS[i]) + " Days:")
            print("Scrobbled Artists: " + lastpage_artists[0])
            print("Scrobbled Tracks: " + lastpage_scrobbles[0])
            print("Average: " + lastavg[0] + "\n")

        # get the current playcount from lastfm overall
        stuff = html.fromstring((requests.get('https://www.last.fm/user/' + USERNAME)).content)
        page_scrobbles = stuff.xpath('//*[@id="content"]/div[2]/header/div[2]/div/div[2]/div[2]/ul/li[1]/p/a/text()')
        cleancount = int(re.sub("[^\\d\\.]", "", page_scrobbles[0])) / int(joineddate() + 1)

        # get the current amount of different artists scrobbled from lastfm overall
        page_artists = requests.get('https://www.last.fm/user/' + USERNAME + '/library/artists')
        stuff_artists = html.fromstring(page_artists.content)
        artists = stuff_artists.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul/li/p/text()')

        # Display the overall average
        print("Overall:")
        print("Scrobbled Artists: " + artists[0])
        print("Scrobbled Tracks: " + page_scrobbles[0])
        print("Passed Days: " + str(int(joineddate() + 1)))
        print("Average: " + str("%.4f" % cleancount))
    except:
        print("\nWhoops, something bugged out, please try again!\n")

if __name__ == "__main__":
    main()
