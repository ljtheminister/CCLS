import subprocess, os, pickle

def getdata(lat,lon,z,link,filename):
    """bla bla bla"""
    from visad import RealType, Real, RealTuple
    from java.lang import Double
    setDebug(1)
    ds = makeDataSource(link)
    temp = getData(ds.getName())
    dc1 = createDisplay('probe',temp)
    pause()
    xyz = dc1.earthToBox(dc1.makeEarthLocation(lat,lon,z))
    dc1.resetProbePosition(xyz[0], xyz[1], xyz[2])
    pause()
    dc1.exportCsvAllTimes(filename)
    return

def parseInput(table):
    timestamp = table[-12:]
    url_date = timestamp[:6] + '/' + timestamp[:8] + '/'
    base_url = 'http://nomads.ncdc.noaa.gov/thredds/dodsC/ndfd/'
    url = base_url + url_date + table
    base_file = os.getcwd()
    filename = base_file + '/' + table + '.csv'
    return (url, filename)

def retrieveList(var):
    table_list = pickle.load(open(var+'.p'))
    return table_list


if __name__ == '__main__':
    x,y,z = 40.78,-73.97,154.0
    '''
    url, filename = parseInput(os.getenv('table'))
    print url
    print filename
    getdata(x,y,z, url, filename)
    '''

    table_list = retrieveList(os.getenv('wx_var'))
    for table in table_list:
	url, filename = parseInput(table)
	getdata(x,y,z, url, filename)


