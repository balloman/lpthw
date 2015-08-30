def midpoint_finder(x1,y1,x2,y2):
     x = x1 + x2
     x = x / 2
     y = y1 + y2
     y = y / 2
     return x, y

print "Welcome to the midpoint calculator."
print "This will help find the midpoint of any two coordinates using the midpoint formula."
print "All i need from you is the coordinates and I will do the rest!"
prompt = ">>> "
print "Now, I need the coordinates of the first point, seperated with enter."
x1 = float(raw_input(prompt))
y1 = float(raw_input(prompt))
print "Now, the coordinates of the second point."
x2 = float(raw_input(prompt))
y2 = float(raw_input(prompt))
print "Thanks, I will start now"
point1, point2 = midpoint_finder(x1,y1,x2,y2)
print point1, ",", point2
