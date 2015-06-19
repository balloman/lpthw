from time import sleep
import os.path

#Editor for the file
def file_editor():
    print "Hello and welcome to the Python file creator."
    print "What is the name file that should be made."
    fname = raw_input(">>> ") + ".txt"
    with open(fname, "w") as f:
        print "What would you like to write in the file"
        s = raw_input(">>> ")
        f.write(s + "\n")
    starter()

def editor():
    try:
        print "Welcome to the editor"
        print "What is the file you would like to open"
        fname = raw_input(">>> ") + ".txt"
        assert (os.path.isfile(fname)), "File does not exist!"
        print "opening file"
        sleep(1.5)
        print "." 
        sleep (1.5)
        print "."
        with open(fname, "r+") as f:
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
            starter()
    except AssertionError:
        print "File does not exist."
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