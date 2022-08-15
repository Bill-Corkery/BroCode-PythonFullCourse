#Lesson 23: Keyword Arguments
# Arguments preceded by an identifier when we pass them to a function
# The order of the arguments does not matte,r unlike positional arguments
# Python knows the names of the arguments that our function receives
# https://www.youtube.com/watch?v=XKHEtdqhLK8

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello("Code", "Dude", "Bro") #these are positional arguments.
hello(last="Code", middle="Dude", first="Bro") #these are keyword arguments.