#Lesson 42: Inheritance
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# classes can inherit attributes and methods from something else (usally another class).
# so if Animal (parent class) is a class with move() and eat().
# then have Dog (subclass/child class) has move(), bark(), and eat().
# move() is overriden. eat(0 is inheritied. Bark() is new.

#will keep all classes in same file for ease.
#the reason want things in parent class if need to make changes,
#only need to do it in one place.

class Animal:
    alive = True
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):  #Rabbit is child class of Animal parent class
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()

#print((rabbit.alive))
#fish.eat()
#hawk.sleep()
