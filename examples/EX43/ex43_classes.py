from sys import exit
from random import randint
from time import sleep



class Scene(object):
    
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n----------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    def enter(self):
        print "Sadly your terrible life has come to an end."
        print "Your ghost leaves your body only to be killed by the ghost-hunters they have brought with them."
        sleep(5)
        exit(1)

class Finished(Scene):
    def enter(self):
        print "Congratulations on beating the game."
        sleep(30)
        exit(0)

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
        prompt = ">>> "
        print "You walk in to see a huge room of weapons."
        print "There are quite a lot of weapons here."
        print 'You see a door that says "Top Secret!" that has a keypad beside it.'
        print "It looks like you need a code to get into the room"
        print "However if you miss the code 6 times, you can't enter it anymore"                                                                         
        print "The code is rom 1-100."
        guesses = 1
        code = randint(1, 100)
        ucode = int(raw_input(prompt))
        while ucode != code and guesses < 6:
            print "That is incorrect"
            if ucode < code:
                print "The code you guessed is lower than the code!"
            elif ucode > code:
                print "The code you guessed is higher than the code!"
            ucode = int(raw_input(prompt))
            guesses += 1
        if guesses == 6 and ucode != code:
            print "You hear the lock fuse as alarms start blaring."
            print "You accept defeat as you slump down to the ground."
            print "Seconds later you are killed by a Gothon's blaster."
            return 'death'
        if ucode == code:
            print "Yay, the code was correct!"
            print "The door opens to a large room filled with Neutron Bombs, the strongest bombs in the known universe."
            print "You grab one and run away as fast as you can(these bombs may look small, but they pack a BIG punch!)"
            print "The first place you go to is the bridge."
            return 'the_bridge'

            





class TheBridge(Scene):
    def enter(self):
        print "You run onto the bridge with the bomb."
        print "There are some gothons there that don't see you."
        print "They hear you walk in and turn around, but are not using thier guns to shoot"
        print ", afraid to detonate the bomb"
        print "You can either slowly drop the bomb at the end of the bridge or throw it and run away."
        action = raw_input(">>> ")
        if "throw it" in action:
            print "You throw it and run"
            print "What you do not know is that all Gothons on the ship are trained in bomb Undetonation."
            print "They quickly shoot you and then disarm the bomb"
            print "You die from your wounds."
            return 'death'
        elif "drop" in action:
            print "You point your blaster at the bomb and slowly walk to the end of the bridge."
            print "They hold their hands up and you drop the bomb at the end and run."
            print "You shoot the lock to lock them inside."
            print "They are too late to react and you get away"
            print "Let's blow this popsicle stand!"
            return 'escape_pod'




class EscapePod(Scene):
    def enter(self):
        print "You run faster than you ever have before to escape the bomb"
        print "You get to the escape pods and there are 5 there"
        print "You dont have time to look and choose one at random."
        ship = int(raw_input(">>> "))
        good_ship = randint(1, 5)
        if ship != good_ship:
            print 'You jump into ship %d and hit the "GO" button' % ship
            print "You slowly see the dials come to life and the vehicle starts shaking."
            print "The pod suddenly shoots off into the air and to space."
            print "You look behind you and see the ship blow into  a million bits and pieces"
            print "MISSION ACCOMPLISHED!"
            sleep(5)
            return 'finished'
        elif ship == good_ship:
            print 'You jump into ship %d and hit the "GO" button' % ship
            print "The dials come to life and the vehicle starts shaking."
            print "..."
            print "Alarms in the pod start blaring as warnings flash on the HUD."
            print "The pod fails to lift and explodes."
            print "You die."
            return 'death'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()