#Lesson 46: Method Chaining
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Method chaining = calling multiple methods sequentially
# each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()
#car.turn_on()
#car.drive()
car.turn_on().drive()
car.brake()\    #this backslash is introduced by program to make it more readable.
    .turn_off()
