## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ##Dog has-a name
        self.name = name


## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        #Cat has a name
        self.name = name


##Person is-a object
class Person(object):

    def __init__(self, name):
        ##person has-a name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary


## Fish is-a object
class Fish(object):
    pass

##Salmon is-a fish
class Salmon(Fish):
    pass

##??
class Halibut(Fish):
    pass


## Rover is-a Dog
rover = Dog("Rover")

##Satan is-a Cat
satan = Cat("Satan")

##Mary is-a Person
mary = Person("Mary")

#Mary has-a cat
mary.pet = satan

##Frank is-an Employee
frank = Employee("Frank", 120000)

##Frank has-a Dog
frank.pet = rover

##Flipper is-a Fish
flipper = Fish()

##crouse is-a Salmon
crouse = Salmon()

##Harry is-a Halibut
harry = Halibut()