#! /usr/local/bin/env python

import urllib2, re, time, pickle
from urllib2 import urlopen
import datetime as dt

dates = []
date = dt.date(2009,01,01)
delta = dt.timedelta(days=1)

while date < dt.date.today():
    dates.append(date)
    date += delta

date_strs = [date.strftime("%Y%m/%Y%m%d") for date in dates]
url_base = 'http://nomads.ncdc.noaa.gov/thredds/dodsC/ndfd/'
url_end = '/catalog.html'

#dict_data = {}
with open("Hist_Temp_Log", "wb") as logfile:
    logfile.write("START: " + str(dt.datetime.now())+'\n')
    
temp_list = []
for ds in date_strs:
    try:
        print ds
        url = url_base + ds + url_end
        catalog = urlopen(url)
        catalog = catalog.readlines()
        search = re.compile("href='catalog.html?.*<tt>YEUZ98.*")
        link_list = filter(search.search, catalog)
        match = re.compile("<tt>.*<")
        table_list = [match.findall(link)[0][4:].split('<')[0] for link in link_list]
        for table in table_list:
            temp_list.append(table)
    except:
        error_str = 'FAILED: ' + str(ds) + ' ' + str(dt.datetime.now())
        print error_str
        with open("Hist_Temp_Log", "a+b") as logfile:
            logfile.write(error_str+'\n')
        

with open("Hist_Temp_Log", "a+b") as logfile:
            logfile.write('FINISHED: '+str(dt.datetime.now())+'\n')
pickle.dump(temp_list, open("temp_list_2009.p", "wb"))











