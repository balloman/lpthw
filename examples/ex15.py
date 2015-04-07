#Importing system commands so I can close the program if I need to.
import time
import sys 
#Just a little art
prompt = '---->'
#Ask for file
print "Put the filename in here with .txt at the end."
filename = raw_input(prompt)
#opens file that was in argument as a text file
txt = open(filename)
print "Opening"
time.sleep(1)
print "."
time.sleep(1)
print "."
time.sleep(1)
print "."
time.sleep(1)
print "Done!"
#Prints out file
print "File ready! %r: Type OK if you want to read it" % filename
choice = raw_input(prompt)
if 'OK' in choice:
    print txt.read()
else:
    print "OK"
    sys.exit()
