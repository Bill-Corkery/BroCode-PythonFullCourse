#Lesson 49: Objects as Arguments
# https://www.youtube.com/watch?v=XKHEtdqhLK8

class Car:
    color = None
class Motorcylce:
    color = None

# make sure this is not within class because then would be a method of car class.
def change_color(vehicle, color): #argument names should be lower case.
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()
bike_1 = Motorcylce()

change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "yellow")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)