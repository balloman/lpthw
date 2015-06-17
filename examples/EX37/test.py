from time import sleep

#Editor for the file
def file_editor():
    print "Hello and welcome to the Python file creator."
    print "What is the name file that should be made."
    fname = raw_input(">>> ") + ".txt"
    f = open(fname, "w")
    print "What would you like to write in the file"
    s = raw_input(">>> ")
    f.write(s + "\n")
    f.close()
    starter()

def editor():
    print "Welcome to the editor"
    print "What is the file you would like to open"
    fname = raw_input(">>> ") + ".txt"
    print "opening file"
    sleep(1.5)
    print "." 
    sleep (1.5)
    print "."
    f = open(fname, "r+")
    sleep(1.5)
    print "."
    sleep(1)
    print "File Opened!"
    sleep(0.5)
    print "File reads."
    print (f.read())
    sleep(0.5)
    print "What would you like to add?"
    s = raw_input(">>> ")
    f.seek(0,2)
    f.write(s + "\n")
    print "File written"
    print "Would you like to save?"
    answer = raw_input(">>> ")
    if "y" in answer:
        print "..."
        sleep(1.25)
        f.close()
        print "File Saved!"
        starter()
    else:
        starter()
#For the start of the program
def start():
    print "Editor or Creator?"
    choice = raw_input(">>> ")
    if "dit" in choice:
        editor()
    else:
        file_editor()

def starter():
    print "Would you like to restart?"
    choice = raw_input(">>> ")
    if "y" in choice:
        print "Restarting"
        sleep(2.11)
        start()
    else:
        print "Bye!"
        sleep(1.5)
        exit()
#Start of the program:)
start()