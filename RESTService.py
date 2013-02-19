'''
    This is the wrapper around the World Bank REST Web Service.
    
'''
# main logic 

import urllib2

regions = {'ARB':'Arab World','EMU':'Euro Area','EUU':'European Union','LDC':'Least Developed Countries',\
           'OED':'OECD Members (Organisation for Economic Co-operation and Development)','WLD':'World',\
           'EAP':'East Asia & Pacific','ECA':'Europe & Central Asia','LAC':'Latin America & Caribbean',\
           'MNA':'Middle East & North Africa','SAS':'South Asia','SSA':'Sub-Saharan Africa','CSS':'Caribbean small states',\
           'OSS':'Other small states','PSS':'Pacific island small states','SST':'Small states'}
           
formats = ('xml', 'json')
           
worldBankURL = 'http://api.worldbank.org/country?per_page=1000&region=%s&format=%s'
countryURL = 'http://api.worldbank.org/countries/%s'

def listRegions() :
    ' This function provides a dictionary of World Bank Regions, {code:name} '
    return regions           

def pullData(request, format) :
    ' This function makes the RESTService call, the region must be valid and the format must be xml or json '
    if request not in regions :
        raise LookupError, "Region: %s not found" % (request)
    if format not in formats :
        raise LookupError, "Format: %s not found" % (format)       
    restURL = worldBankURL % (request, format)
    response = urllib2.urlopen(restURL).read()
    return response
    
def pullCountryData(request) :
    ' This function makes the RESTService call, the country code must be valid '
    restURL = countryURL % (request)
    try :
        response = urllib2.urlopen(restURL).read()
    except :
        raise LookupError, "Country: %s not found" % (request)     
    return response
    
if __name__ == '__main__' :

    # my tests
    # tests for listRegions()
    if not len(listRegions()) == 16 : raise AssertionError, "listRegions not returning 16"
   
    # tests for pullData
    pullData('ARB', 'xml')   #  these should work
    pullData('PSS', 'json') 
   
    try :
        pullData(None, 'xml')  # this should fail
        raise AssertionError, "pulled 'None' region"
    except LookupError :
        pass            # do nothing, expected
    try :
        pullData('SAS', None)  # this should fail
        raise AssertionError, "pulled 'None' format"
    except LookupError :
        pass            # do nothing, expected        
    
    if not len(pullData('SAS', 'xml')) > 0 : raise AssertionError, "no data returned from REST call"
    if not len(pullData('EUU', 'json')) > 0 : raise AssertionError, "no data returned from REST call"
    
    # tests for pullCountryData   
    pullCountryData('br')   # these should work
    pullCountryData('ca')   
    
    try :
        pullCountryData(None)  # this should fail
        raise AssertionError, "pulled 'None' country"
    except LookupError :
        pass            # do nothing, expected
    try :
        pullData('XY')  # this should fail
        raise AssertionError, "pulled 'XY' format"
    except LookupError :
        pass            # do nothing, expected     
    
