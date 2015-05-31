from sys import exit
import time
import encounter

#Hp at start of game
hp = 100
#The prompt for inputs
prompt = "> "

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
encounter.bear(hp)

#Start of second encounter
print "You continue walking and see a killer bee approaching you"
print "What do you do"
print "run away, swat the bee away"
