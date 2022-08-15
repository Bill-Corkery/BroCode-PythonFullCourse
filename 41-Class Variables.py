#Lesson 41: Class Variables
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# class variable is declared inside class and is default normally.
# instance variable is declared inside a constructor. Has unique value.

from car import Car
car_1 = Car("Chevy", "Corvette", 2021, 'blue')
car_2 = Car("Ford", "Mustang", 2022, 'red')

#Car.wheels = 2  #this changes all default wheels number
