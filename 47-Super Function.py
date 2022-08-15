#Lesson 47: Super Function
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# super() = Function used to give access to the methods of a parent class.
# Returns a temporary object of a parent class when used.

#so with below, any similarities between square and cube,
# can move to rectangle. This will decrease repeat code.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__(self,length, width, height):
        super().__init__(length, width)
        self.height = height
    def volumne(self):
        return self.length*self.width*self.height

square = Square(3,3)
cube = Cube(3,3,3)
print(square.area())
print(cube.volumne())