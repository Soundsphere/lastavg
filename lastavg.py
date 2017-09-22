#!/usr/bin/env python
# Shows all scrobbling info for the last 7, 30, 90, 180, 360 days as well as
# the scrobbled artist for that timeframe along with the average scrobbles

from datetime import datetime
import time
import re
import requests
import os
import configparser
from lxml import html

# set a few things like days, the integer for the for loop and home directory
DAYS = 7, 30, 90, 180, 365
D = len(DAYS)
HOME = os.environ['HOME']
BASE = 'https://www.last.fm/user/'

# inital setup
def configure():
    """
    Setup and configuration

    Sets up a config file in %HOME/.config/lastavg to store the username and joined date
    This function gets executed when the program is run the first time
    """
    if not os.path.exists(HOME + "/.config/lastavg/config.cfg"):
        os.makedirs(HOME + "/.config/lastavg/")
        username = input("What's your last.fm username? ")
        while True:
            try:
                joined_date = input("When did you join last.fm? ")
                datetime.strptime(joined_date, '%d.%m.%Y')
                break
            except KeyboardInterrupt:
                raise
            except:
                print("\nPlease use DD.MM.YYYY as the date format\n")
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'user': username,
                            'joined': joined_date}
        with open(HOME + '/.config/lastavg/config.cfg', 'w') as configfile:
            config.write(configfile)

# Get the days between today and the lastfm JOINED date
def joineddate():
    """
    Return the days on last.fm.

    Takes the JOINED constant and calculates the days on lastm.
    """
    config = configparser.ConfigParser()
    config.read(HOME + '/.config/lastavg/config.cfg')
    date_format = "%d.%m.%Y"
    date_joined = datetime.strptime(config['DEFAULT']['joined'], date_format)
    today = datetime.strptime(time.strftime("%d.%m.%Y"), date_format)
    delta = today - date_joined
    return delta.days + 1

def main():
    # Check if config file is there and load it
    if os.path.exists(HOME + '/.config/lastavg/config.cfg'):
        config = configparser.ConfigParser()
        config.read(HOME + '/.config/lastavg/config.cfg')
    else:
        configure()
        config = configparser.ConfigParser()
        config.read(HOME + '/.config/lastavg/config.cfg')

    # Print some sort of header
    print("Stats for " + config['DEFAULT']['user'] + ":\n")

    # This for-loop iterates 5 times to get the average, the playcount and the scrobbled artists for
    # each number of days stored in the days tuple and displays the output
    try:
        for i in range(D):
            lastpage_scrobbles = requests.get( BASE + config['DEFAULT']['user'] + '/library?date_preset=LAST_' + str(DAYS[i]) + '_DAYS')
            lastpage_artists = requests.get( BASE + config['DEFAULT']['user'] + '/library/artists?date_preset=LAST_' + str(DAYS[i]) + '_DAYS')
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
        stuff = html.fromstring((requests.get(BASE + config['DEFAULT']['user'])).content)
        page_scrobbles = stuff.xpath('//*[@id="content"]/div[2]/header/div[2]/div/div[2]/div[2]/ul/li[1]/p/a/text()')
        cleancount = int(re.sub("[^\\d\\.]", "", page_scrobbles[0])) / int(joineddate() + 1)

        # get the current amount of different artists scrobbled from lastfm overall
        page_artists = requests.get(BASE + config['DEFAULT']['user'] + '/library/artists')
        stuff_artists = html.fromstring(page_artists.content)
        artists = stuff_artists.xpath('//*[@id="mantle_skin"]/div[4]/div/div[1]/ul/li/p/text()')

        # Display the overall average
        print("Overall:")
        print("Scrobbled Artists: " + artists[0])
        print("Scrobbled Tracks: " + page_scrobbles[0])
        print("Passed Days: " + str(int(joineddate() )))
        print("Average: " + str("%.4f" % cleancount))
    except:
        print("\nWhoops, something bugged out, please try again!\n")

if __name__ == "__main__":
    main()
