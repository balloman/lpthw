name = 'Zed A. Shaw'
age = 35
dyears = age * 7
height = 74
centimeter = height * 2.54
weight = 180
kilos = weight * 0.45
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Lets talk about %s." % name
print "He's %d inches tall.(%d cenitmeters) " % (height, centimeter)
print "He's %d pounds heavy(%d kilograms)." % (weight, kilos)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth


print "If i add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)