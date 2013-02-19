'''
    This represents a Country object within the World Bank REST Web Service
    
'''

from xml.dom.minidom import Document

class Country :
    def __init__(self,code=None,name=None,capital=None,lat=None,lon=None) :
        ' The Country Constructor '
        self.__code = code
        self.__name = name
        self.__capital = capital
        self.__lat = lat
        self.__lon = lon   

    def setCode(self, code) :
        '  Mutator for Code '
        self.__code = code

    def getCode(self) :
        '  Accessor for Code '
        return self.__code
    
    def setName(self, name) :
        '  Mutator for Name '
        self.__name = name

    def getName(self) :
        '  Accessor for Name '
        return self.__name
        
    def setCapital(self, capital) :
        '  Mutator for Capital '
        self.__capital = capital

    def getCapital(self) :
        '  Accessor for Capital '
        return self.__capital        
    
    def setLon(self, lon) :
        '  Mutator for Longitude '
        self.__lon = lon

    def getLon(self) :
        '  Accessor for Longitude '
        return self.__lon
        
    def setLat(self, lat) :
        '  Mutator for Latitude '
        self.__lat = lat

    def getLat(self) :
        '  Accessor for Latitude '
        return self.__lat
        
    def getAsXML(self) :
        '''
        return this Country object as XML
         
        <country>
            <code>GR</code>
            <name>Greece</name>
            <capital>
                <city>Athens</city>
                <longitude>23.7166</longitude>
                <latitude>37.9792</latitude>  
            </capital>
        </country>
        
        '''
        doc = Document()
        countryElement = doc.createElement("country")
        doc.appendChild(countryElement)
        
        codeElement = doc.createElement("code")
        codeText = doc.createTextNode(self.__code)
        codeElement.appendChild(codeText)
        countryElement.appendChild(codeElement)
        
        nameElement = doc.createElement("name")
        nameText = doc.createTextNode(self.__name)
        nameElement.appendChild(nameText)
        countryElement.appendChild(nameElement)
        
        capitalElement = doc.createElement("country")
        
        cityElement = doc.createElement("city")
        cityText = doc.createTextNode(self.__capital)
        cityElement.appendChild(cityText)
        capitalElement.appendChild(cityElement)
        
        lonElement = doc.createElement("longitude")
        lonText = doc.createTextNode(self.__lon)
        lonElement.appendChild(lonText)
        capitalElement.appendChild(lonElement)
        
        latElement = doc.createElement("latitude")
        latText = doc.createTextNode(self.__lon)
        latElement.appendChild(latText)
        capitalElement.appendChild(latElement)
        
        countryElement.appendChild(capitalElement)
        
        return doc.toprettyxml(indent="  ")

        
    def __str__(self) :
        ' the ToString function '
        output = "%s-%s [Capital: %s @ %s Latitude %s Longitude]" % (self.__code, self.__name, self.__capital, self.__lon, self.__lat)
        return output
        
if __name__ == '__main__' :

    # my tests
    # tests for __str__()
    country = Country('CA', "Canada", 'Owatta', '43.433', '-75.71')
    expected = "CA-Canada [Capital: Owatta @ -75.71 Latitude 43.433 Longitude]"

    if not str(country) == expected : raise AssertionError, "Country __str__ incorrect"
        
