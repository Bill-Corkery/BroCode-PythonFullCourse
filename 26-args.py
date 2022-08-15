#Lesson 26: *args
# parameter that will pack all arguments into a tuple (ordered, unchangable).
# useful so that a function can accept a varying amount of arguments.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

def add(*stuff):
    sum = 0
    #stuff = list(stuff) # if want to change an item in tuple, turn into list.
    #stuff[0] = 0    # this turns the 1st item to 0.
    for i in stuff:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7,8))