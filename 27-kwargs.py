#Lesson 27: **kwargs
# parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword arguments
# https://www.youtube.com/watch?v=XKHEtdqhLK8

def hello(**kwargs):  #just need the two **. Dont need to name it kwargs.
    print("Hello "+ kwargs['first']+" "+kwargs['last'])
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value, end= " ")  #end=" " replaces the new line character (default) with space.

hello(title="Mr.", first="Bro", middle="Dude", last="Code")