#Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

def prompt():
    print '-' * 10

#Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#Print some states
print '-' * 10
print "Michigan's abbreviatoin is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#Do it by using the sate then cities dict
prompt()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#Print every state abbreviation
prompt()
for state, abbrev in states.items():
    print "%s is abbrevaited %s" % (state, abbrev)

#Print every city in state
prompt()
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

#Now do both at the same time
prompt()
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

prompt()
#Safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print "Sorry, no Texas."

#Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX is: %s" % city