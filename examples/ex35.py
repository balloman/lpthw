from sys import exit
import time

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
        
  
def choices():
    time.sleep(1)
    print "take honey"
    time.sleep(1)
    print "taunt bear"
    time.sleep(1)
    print "open door"
        
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        choices()
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. It looks at you suspiciously."
        elif next == "open door" and not bear_moved:
            print dead("The bear eats your face off and spreads honey on it as a topping.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "That isn't one of the choices I gave you."


def cthulu_room():
    print "Here you see the great evil Ctuhulu."
    time.sleep(1)
    print "He stares at you and you go insane."
    time.sleep(1)
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        print "Omnomnom"
        time.sleep(1)
        dead('"Well that was tasty," exclaims the Ctuhulu')
    else:
        print "Well, do something!!!"
        cthulu_room()


def dead(why):
    print why, "Good Job!"
    exit(0)

def start():
    print "You are in a dark room."
    time.sleep(1)
    print "There is a door to your right and left."
    time.sleep(1)
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()