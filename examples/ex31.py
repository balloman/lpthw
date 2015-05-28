import time

print "You enter a dark room with two doors. Do you go through door one or door two?"

door = raw_input("Which door? ")

if "1" in door:
    print "There is a giant bear here eating a cheesecake. What do you do?"
    time.sleep(3)
    print "-----"
    print "1. Take the cake."
    time.sleep(2)
    print "-----"
    print "2. Scream at the bear."
    
    bear = raw_input("What do you do? ")
    
    if bear == "1":
        print "The bear eats your face off. Good job." 
    elif bear == "2":
        print "The bear eats your leg off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
        
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "----------------"
    time.sleep(1)
    print "1. Blueberries."
    time.sleep(1)
    print "-----------------"
    time.sleep(1) 
    print "2. Yellow jacket Clothespins."
    time.sleep(1)
    print "-----------------"
    time.sleep(1)
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        time.sleep(1)
        print "Your body survives powered by a mind of jello."
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"
        
else:
    print "You stumble around and fall on a knife and die. Stupid fucking itdiot." 