#!/usr/bin/env python
# this thing lets me calculate the average songs I played since I joined lastfm.
# Sure, the website tells me as well, but I want to have at least a few
# decimals, to see the changes.

from datetime import date, datetime
import time
from lxml import html
import requests
import re

# Get the days between today and my lastm joined date
date_format = "%d/%m/%Y"
date_joined = datetime.strptime('09/1/2009', date_format)
today = datetime.strptime(time.strftime("%d/%m/%Y"), date_format)
delta = today - date_joined

# get the current playcount from lastfm
page = requests.get('https://www.last.fm/user/StonedEars')
tree = html.fromstring(page.content)
playcount = tree.xpath('//*[@id="content"]/div[2]/header/div[2]/div/div[2]/div[2]/ul/li[1]/p/a/text()')
cleancount = int(re.sub("[^\d\.]", "", playcount[0])) / int(delta.days + 1)

# Display the stuff
print ("Played Tracks: " + playcount[0])
print ("Passed Days: " + str(int(delta.days + 1)))
print ("Average: " + str("%.4f" % cleancount))
