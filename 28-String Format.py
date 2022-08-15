#Lesson 28: String Format
# str.format() = optional method that gives users more control when displaying outputs
# https://www.youtube.com/watch?v=XKHEtdqhLK8

animal = "cow"
item = "moon"
#print("The "+animal+" jumped over the "+item)  better way to write this is below.
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))  #positional argument
print("The {food} jumped over the {house}".format(house="tall", food="pizza"))  #keyword argument

#another way to format:
text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Bro"
print("Hello, my name is {}".format(name)) #can add some padding.
print("Hello, my name is {:10}".format(name))  #adding ten spacing worth of padding after name.
print("Hello, my name is {:^10}".format(name)) #added center align. Can do right > or left <

number = 1000
print("The number pi is {:.3f}".format(number))  #adds 3 deciminal places.
print("The number is {:,}".format(number)) #adds commas
print("The number is {:b}".format(number)) #displays it in binary
print("The number is {:o}".format(number)) #displays it in octodecimal
print("The number is {:X}".format(number)) #displays it in hexidicimal.
print("The number is {:E}".format(number))