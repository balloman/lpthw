try:
    print "My name is Bernard."
    print "Type the number 5 here."
    number = raw_input()
    if number != 5:
        raise SyntaxError("Hi")
except SyntaxError:
    print "Hi."
finally:
    print "Sorry"