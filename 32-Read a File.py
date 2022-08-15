#Lesson 32: Read a File
# this will read a file. need to created a plain text file called test.txt in project folder
# https://www.youtube.com/watch?v=XKHEtdqhLK8

try:
    with open('test.txt') as file:  #will need file path and double-slashes if not here.
        print(file.read())  #'with' will also close file after reading them.
except FileNotFoundError:
    print("That file was not found")