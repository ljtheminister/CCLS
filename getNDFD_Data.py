import subprocess, os

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

if __name__ == '__main__':
    x,y,z = 40.78,-73.97,154.0

    table = sys.argv[1]
    timestamp = table[-12:]
    url_date = timestamp[:6] + '/' + timestamp[:8] + '/'
    url = base_url + url_date + table
    filename = base_file + '/' + table + '.csv'
    base_url = 'http://nomads.ncdc.noaa.gov/thredds/dodsC/ndfd/'
    
    getdata(x,y,z)



