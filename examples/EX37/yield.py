try:
    a = raw_input()
    b = raw_input()
    answer = a/b
except ZeroDivisionError:
    print "You idiot, you can't divide by zero!"
except TypeError:
    print "You can't divide letters stupid!"
except:
    print "Unknown Error"
else:
    print answer