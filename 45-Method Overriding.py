#Lesson 45: Method Overriding
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# method overridding is when a subclass (or child class)
# can override a method of its parent class.

#animal is parent class and rabbit is child class.
class Animal:
    def eat(self):
        print("This animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()
