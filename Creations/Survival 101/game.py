from sys import exit
from time import sleep
import time

#Hp at start of game:
hp = 100

#Bear encounter
def bear(hp):
    choice = raw_input("> ")
    if "stand" in choice:
        print "The bear walks off, and you continue on your way"
    elif "run" in choice:
        print "..."
        time.sleep(2)
        print "The bear chases you and your face gets mauled."
        print "You barely make it out alive, however you have sustained serious damage"
        hp = hp-60
        currenthp(hp)
    elif "agressive" in choice:
        print "..."
        time.sleep(2)
        print "The bear sees you as a threat and attacks you."
        print "The bear nearly kills you and you are almost dead"
        hp = hp-90
        currenthp(hp)
    else:
        print "Well do something!"
#Bee encounter
    

    
#Function to display the current hp of the current player
def currenthp(hp):
    if hp < 100:
        print "Your hp is now at %d" % hp
    elif hp <= 0:
        dead()
    else:
        print "You are still healthy, good job!"
        
#Called when player dies
def dead():
    print "You sustained too much damage, and as a result have died."
    time.sleep(3)
    print "GAME OVER!"
    print "Would you like to play again?"
    choice = raw_input("> ")
    if "y" in choice:
        start_game()
    else:
        exit(0)



#The prompt for inputs
prompt = "> "

 #Called to Start the Game, useful for restarting the program       
def start_game():
    print "Welcome to Survival 101"

#Description of game
start_game()
print "You start your regular trail."
print "It will be just a little different this time though ;)"

#Start of game
time.sleep(3)
print "You are walking along when suddenly."
time.sleep(1)
print "..."
time.sleep(2)

#Start of first encounter
print "Wild bear appears!."
print "What do you do?"
print "Stand your ground, Run away, be agressive in an attempt to scare the bear"

#first encounter
bear(hp)

#Start of second encounter
print "You continue walking and see a killer bee approaching you"
print "What do you do"
print "run away, swat the bee away"
