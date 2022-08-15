#Lesson 52: Functions to Variables
# https://www.youtube.com/watch?v=XKHEtdqhLK8

#This defines the function
def hello():
    print("Hello")

#this calls the function.
hello()

#this will pring the location of the function in memory. It changes.
print(hello)
#these will be the same location as it is basically a function with two alias or names (hi and hello)
hi = hello
print(hi)

say = print  #this is assigning print function to a variable.
say("What! I cannot believe this works!")