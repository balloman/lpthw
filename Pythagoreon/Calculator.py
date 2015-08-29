import math
#I put the formula here for simplicity and practice defining methods.
def distancecalc(x2, x1, y2, y1):
    x=x2-x1
    x=math.pow(x, 2)
    y=y2-y1
    y=math.pow(y, 2)
    xysquare = x+y
    distance = math.sqrt(xysquare)
    return distance
    

print "Hi, this is a free distance calculator for Algebra. Just put in the points and I will do it for you."
print "Put x2 in here and x1 after that."
x2=float(raw_input())
print "Alright now the second number"
x1=float(raw_input())
print "Now I need y2"
y2=float(raw_input())
print "Okay, enter y1"
y1=float(raw_input())
print "Alright I'm going to get the number now"
#Running the method now
printed = distancecalc(x2, x1, y2, y1)
print "The distance is "
print printed
print "."