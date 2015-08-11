from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        pass

class Engine(object):
    def __init__(self, scene_map):
        pass
    def play(self):
        pass

class Death(Scene):
    def enter(self):
        print "Sadly your terrible life has come to an end."
        print "Your ghost leaves your body only to be killed by the ghost-hunters they have brought with them."
        exit()

class CentralCorridor(Scene):

    def enter(self):
        print "There is a Gothon standing here and the only way to defeat him is with a joke."
        self.prompt = "> "
        print "Tell him a joke."
        joke = raw_input(self.prompt)
        if len(joke) > 10:
            print "Success!!"
            print "The Gothon laughs at your joke and you blast him with your gun before he can react."
            return 'laser_weapon_armory'
        else:
            print "Joke was not good enough"
            print "You die for bad joke!!!"
            return 'death'

class LaserWeaponArmory(Scene):
    def enter(self):
        self.prompt = ">>> "
        print "You walk in to see a huge room of weapons."
        print "There are quite a lot of weapons here."
        print 'You see a door that says "Top Secret!" that has a keypad beside it.'
        print "It looks like you need a code to get into the room"                                                                         
        print "The code is 4 digits."
        digit1 = randint(1, 9)
        digit2 = randint(1, 9)
        digit3 = randint(1, 9)
        digit4 = randint(1, 9)
        self.message = "Each digit is a number from 1-9"
        print "Each digit is a number from 1-9"
        print "Guess all the digits to open the door"
        udigit1 = int(raw_input(self.prompt))
        udigit2 = int(raw_input(self.prompt))
        udigit3 = int(raw_input(self.prompt))
        udigit4 = int(raw_input(self.prompt))
        if udigit1 == digit1:
            correct1 = True
        elif udigit1 > digit1:
            print "Your number is greater that the 1st digit."
        elif udigit1 < digit1:
            print "Your 1st digit is smaller than the 1st digit."
        elif udigit1 > 9:
            print self.message
            return 'laser_weapon_armory'
        if udigit2 == digit2:
            correct1 = True
        elif udigit2 > digit2:
            print "Your number is greater that the 1st digit."
        elif udigit2 < digit2:
            print "Your 1st digit is smaller than the 1st digit."
        elif udigit2 > 9:
            print self.message
            return 'laser_weapon_armory'
        if udigit3 == digit3:
            correct1 = True
        elif udigit3 > digit3:
            print "Your number is greater that the 1st digit."
        elif udigit3 < digit3:
            print "Your 1st digit is smaller than the 1st digit."
        elif udigit3 > 9:
            print self.message
            return 'laser_weapon_armory'
        if udigit4 == digit3:
            correct1 = True
        elif udigit4 > digit3:
            print "Your number is greater that the 1st digit."
        elif udigit4 < digit3:
            print "Your 1st digit is smaller than the 1st digit."
        elif udigit4 > 9:
            print self.message
            return 'laser_weapon_armory'



class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene_name):
        pass
    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()