#Lesson 40: Object Oriented Programming (OOP)
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# object is an instance of a class. Combination of attributes (what object is/has, e.g. tall) and
# methods (what object can do, e.g. sleep).

#if program is large, pull class in a seperate module.
# Dont need to pass in self into class.

from car import Car
car_1 = Car("Chevy", "Corvette", 2021, 'blue')
# print(car_1.make)
car_2 = Car("Ford", "Mustang", 2022, 'red')

car_1.drive()
car_2.stop()