#Lesson 57: Filter
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# filter() = creates a collection of elements from an iterable for which a function returns True
# filter(function, iterable) so it accepts two arguments

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phobe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

age = lambda data:data[1] >= 18
drinking_buddies = list(filter(age, friends))  # the list() is casting it back into a new list, drinking_buddies
for i in drinking_buddies:
    print(i)