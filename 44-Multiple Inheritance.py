#Lesson 44: Multiple  Inheritance
# https://www.youtube.com/watch?v=XKHEtdqhLK8
#Multiple Inheritance = when a child class is derived from more than one parent class

#this is used when want to create a class that needs different attributes/methods from multiple classes.
#so below some animals are both prey and predator (e.g. fish)
class Prey:
    def flee(self):
        print("This animal flees")
class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

#as can be seen below, only fish has flee and hunt.
#rabbit.flee()
#hawk.hunt()
#fish.hunt()
#fish.flee()