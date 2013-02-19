#
# A Python wrapper around the WorldBank REST API
#

import WorldBank   # import the WorldBank package

print ''' 
    Please select a Region using the Codes below:
    '''

regions = WorldBank.getListOfRegions()
for key, value in regions.items() :
    print '\t', key, ' - ', value
    
print "\n"
input = raw_input("Your Selection: ") 

print input

print "Please select a Country (by number):"
results = WorldBank.getListOfCountriesByRegion(input)
for (i,x) in enumerate(results) :
    print "%3d:\t%s - %s" % ((i + 1), x.getCode(), x.getName()) 

input = raw_input("Your Selection: ") 

selection = results[int(input) - 1]

print selection

