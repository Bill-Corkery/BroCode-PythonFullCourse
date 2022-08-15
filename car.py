#Lesson 40: Object Oriented Programming (OOP)
# https://www.youtube.com/watch?v=XKHEtdqhLK8
class Car:
    wheels = 4 #class default varaiable.
    def __init__(self, make,model, year, color):
        self.make = make    #instance variables
        self.model = model  #instance variables
        self.year = year    #instance variables
        self.color = color  #instance variables
    def drive(self):
        print("This "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" is stopped")