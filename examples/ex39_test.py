import hashmap
from hashmap import prompt

#create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

#create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'Sand Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

#add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')


#print out some cities
prompt()
print "NY State has : %s" % hashmap.get(cities, 'NY')
print "OR has: %s" % hashmap.get(cities, 'OR')

#Print some states
prompt()
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

#do it by using the state the cities dict
prompt()
print "Michigan has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

#Print every state abbreviation
prompt()
hashmap.list(states)

#Print every city in states
prompt()
hashmap.list(cities)

prompt()
state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas."

#default values using ||= with the nil result
#Can you do this on one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city