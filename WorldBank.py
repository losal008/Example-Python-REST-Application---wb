'''
    This is public API for the WorldBank Package
    
'''

import RESTService
from Country import Country
from xml.dom.minidom import parseString
import math

def getListOfRegions() :
    ' This returns the Regions as a dictionary '
    return RESTService.listRegions() 
    
def getListOfRegionCodes() :
    ' This returns the Regions Code as a list '
    return RESTService.listRegions().keys() 
    
def getRegionDataAsXML(region) :
    ' returns all the Region data as XML '
    return RESTService.pullData(region, 'xml')    
    
def getRegionDataAsJSON(region) :
    ' returns all the Region data as Json '
    return RESTService.pullData(region, 'json')  
    
def getListOfCountryNamesByRegion(region) :
    ' returns list of Country names by Region '     
    dom = parseString(RESTService.pullData(region, 'xml'))
    results = list()  
    xmlTags = dom.getElementsByTagName('wb:name')
    for entry in xmlTags :  
        record = entry.toxml()
        xmlData=record.replace('<wb:name>','').replace('</wb:name>','')
        results.append(xmlData.encode('ascii'))
    return results
    
def getListOfCountriesByRegion(region) :
    ' returns list of Country objects by Region '     
    dom = parseString(RESTService.pullData(region, 'xml'))
    results = list()  
    xmlTags = dom.getElementsByTagName('wb:country')
    for entry in xmlTags :  
        code = entry.getElementsByTagName('wb:iso2Code')[0]
        codeXML = code.toxml()
        codeData = codeXML.replace('<wb:iso2Code>','').replace('</wb:iso2Code>','')
        name = entry.getElementsByTagName('wb:name')[0]
        nameXML = name.toxml()
        nameData = nameXML.replace('<wb:name>','').replace('</wb:name>','')
        city = entry.getElementsByTagName('wb:capitalCity')[0]
        cityXML = city.toxml()
        cityData = cityXML.replace('<wb:capitalCity>','').replace('</wb:capitalCity>','')
        lon = entry.getElementsByTagName('wb:longitude')[0]
        lonXML = lon.toxml()
        lonData = lonXML.replace('<wb:longitude>','').replace('</wb:longitude>','')
        lat = entry.getElementsByTagName('wb:latitude')[0]
        latXML = lat.toxml()
        latData = latXML.replace('<wb:latitude>','').replace('</wb:latitude>','')
        country = Country(codeData, nameData, cityData, lonData, latData) 
        results.append(country)
    return results

def getCountryByCode(code) :
    ' returns a Country object for a specific code '
    dom = parseString(RESTService.pullCountryData(code))
    xmlTags = dom.getElementsByTagName('wb:country')[0] 
    code = xmlTags.getElementsByTagName('wb:iso2Code')[0]
    codeXML = code.toxml()
    codeData = codeXML.replace('<wb:iso2Code>','').replace('</wb:iso2Code>','')
    name = xmlTags.getElementsByTagName('wb:name')[0]
    nameXML = name.toxml()
    nameData = nameXML.replace('<wb:name>','').replace('</wb:name>','')
    city = xmlTags.getElementsByTagName('wb:capitalCity')[0]
    cityXML = city.toxml()
    cityData = cityXML.replace('<wb:capitalCity>','').replace('</wb:capitalCity>','')
    lon = xmlTags.getElementsByTagName('wb:longitude')[0]
    lonXML = lon.toxml()
    lonData = lonXML.replace('<wb:longitude>','').replace('</wb:longitude>','')
    lat = xmlTags.getElementsByTagName('wb:latitude')[0]
    latXML = lat.toxml()
    latData = latXML.replace('<wb:latitude>','').replace('</wb:latitude>','')
    return Country(codeData, nameData, cityData, lonData, latData) 
    
def compareCapitals(country1, country2) :
    '''
     returns an approximation of the direction between two capital cities
     Using the Haversine formula for distance and the forward azimuth formula for bearing 	
             
    '''
    
    lat1 = float(country1.getLat())
    lon1 = float(country1.getLon())
    lat2 = float(country2.getLat())
    lon2 = float(country2.getLon())
    radius = 6378 # 3963 miles 6378 km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c
    
    y = math.sin(lon2) * math.cos(lat1);
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2);
    bearing = math.degrees(math.atan2(y, x));
    
    return (distance, bearing)
    

if __name__ == '__main__' :

    # my tests
    print getRegionDataAsXML('SAS')
    print getRegionDataAsJSON('SAS')   
    print getListOfCountryNamesByRegion('SAS')
    for entry in getListOfCountriesByRegion('SAS') :
        print entry
    print getCountryByCode('br')
    
    print compareCapitals(getCountryByCode('br'), getCountryByCode('mx'))
