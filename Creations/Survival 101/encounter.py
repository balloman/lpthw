import time

#Bear encounter
def bear(hp):
    import game
    choice = raw_input("> ")
    if "stand" in choice:
        print "The bear walks off, and you continue on your way"
    elif "run" in choice:
        print "..."
        time.sleep(2)
        print "The bear chases you and your face gets mauled."
        print "You barely make it out alive, however you have sustained serious damage"
        hp = hp-60
        game.currenthp(hp)
    elif "agressive" in choice:
        print "..."
        time.sleep(2)
        print "The bear sees you as a threat and attacks you."
        print "The bear nearly kills you and you are almost dead"
        hp = hp-90
        game.currenthp(hp)
    else:
        print "Well do something!"
#Bee encounter
    