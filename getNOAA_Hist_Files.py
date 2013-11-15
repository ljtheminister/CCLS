#! /usr/local/bin/env python

import urllib2, re, time, pickle
from urllib import urlopen
import datetime as dt

dates = []
date = dt.date(2009, 1, 1)
delta = dt.timedelta(days=1)
last_day = dt.date(2013, 8, 26)

while date < last_day: 
    dates.append(date)
    date += delta

date_strs = [date.strftime("%Y%m/%Y%m%d") for date in dates]
url_base = 'http://nomads.ncdc.noaa.gov/thredds/dodsC/ndfd/'
url_end = '/catalog.html'

with open("Hist_Cloud_Log", "wb") as cloud_logfile

#temp_list = []
cloud_list = []
dewpt_list = []

temp_regexp = "href='catalog.html?.*<tt>YEUZ98.*"
cloud_regexp = "href='catalog.html?.*<tt>YAUZ98.*"
dewpt_regexp = "href='catalog.html?.*<tt>YFUZ98.*"

def filterCatalog(catalog, regexp):
    search = re.compile(regexp)
    link_list = filter(search.search, catalog)
    match = re.compile("<tt>.*<")
    table_list = [match.findall(link)[0][4:].split('<')[0] for link in link_list]
    return table_list

for ds in date_strs[:2]:
    try:
	print ds
        url = url_base + ds + url_end
        catalog = urlopen(url)
        catalog = catalog.readlines()
    except:
	print 'Link Issue'

    try:
	cloud_list += filterCatalog(catalog, cloud_regexp)
    except:
	print 'cloud issue'

    try:
	dewpt_list += filterCatalog(catalog, dewpt_regexp) 
    except:
	print 'dewpt issue'	



