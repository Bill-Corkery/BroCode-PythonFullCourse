#Lesson 20: Index operator []
# gives access to a sequence's element (str, list, tuples)
# https://www.youtube.com/watch?v=XKHEtdqhLK8

name = "bro Code!"
if(name[0].islower()):
    name = name.capitalize()
print(name)

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)