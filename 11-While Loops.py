#Lesson 11: While loops = a statement that will execute
#its block of code, as long as its condition remains true.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

#will try to create a loop for user to enter name.
# need an escape to the while loop

#To start a code execution below, Ctrl + F5
#To stop a code execution below, Ctrl + F2

name = ""
while len(name) == 0:
    name = input("Enter your name: ")
print("Hello "+name)

#another way to write this:
name = None
while not name:
    name = input("Enter your name: ")
print("Hello "+name)