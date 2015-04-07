#Importing system commands so I can close the program if I need to.
import time
import sys 
import os
#Just a little art
prompt = '---->'
#Ask for file
print "Put the filename in here with .txt at the end. If it doesn't exit, I will create it for you!"
filename = raw_input(prompt)
#opens file that was in argument as a text file
print "Opening"
time.sleep(0.5)
print "."
time.sleep(0.5)
print "."
time.sleep(0.5)
print "."
time.sleep(0.5)
print "Done!"
#Prints out file
print "File ready! %r: Type 'ok' if you want to edit it" % filename
choice = raw_input(prompt)
if 'ok' in choice:
    print "What would you like to write in the file?"
    fedit = raw_input(prompt)
    print "Would you like a backup of the file?"
    choice2 = raw_input(prompt)
    if 'yes' in choice2 :
        os.rename(filename, filename + '_backup')
        print "Backup made!"
        time.sleep(2)
    else:
        print "Oooookkkkk"
        time.sleep(2)
    print "Now writing to file"
    print "."
    with open(filename, 'w+') as f:
        infile = f.read
        print infile
        time.sleep(5)
        f.write(fedit)
        time.sleep(1)
        print "."
        print "Saving file"
        time.sleep(1)
        print "."
        time.sleep(1)
        print "."
        time.sleep(1)
        print "."
        time.sleep(1)
        f.close
        print "Done!"
        print "Now closing"
        time.sleep(3)
        sys.exit()
        
    
else:
    print "OK"
    sys.exit()