#Lesson 48: Abstract Classes
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Prevents a user from creating an object of that class +
# compels a user to override abstract methods in a child class.
# basically a form of checks and balances

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but doe not have an implementation.

from abc import ABC, abstractmethod
class Vehicle(ABC):  #this is class.
    @abstractmethod   #this is a decorator.
    def go(self):  #this is the method.
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#if try to run this, get typeerror because abstract class.
#vehicle.go()
car.go()
car.stop()
motorcycle.go()
motorcycle.stop()