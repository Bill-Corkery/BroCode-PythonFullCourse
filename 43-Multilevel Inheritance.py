#Lesson 43: Multilevel Inheritance
# https://www.youtube.com/watch?v=XKHEtdqhLK8
#Multi-level inerhtiance = when a derived (child) class inherits from
#another derived (child) class

class Organism:
    alive = True
class Animal(Organism):
    def eat(self):
        print("This Animal is eating")
class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()