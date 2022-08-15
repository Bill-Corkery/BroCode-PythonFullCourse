#Lesson 8: String Slicing
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# slicing = create a substring by extracing elements from
# another string. indexing[] or slice()
# [start:stop:step]
# start index in inclusive. stop index is exclusive.
# step is how much increasing index. default is 1.

name = "Bro Code"
first_name = name[:3]
last_name = name[4:]
funky_name = name[::3]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(funky_name)

website1 = 'http://test.com'
website2 = 'http://google.com'
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])
