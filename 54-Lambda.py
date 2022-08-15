#Lesson 54: Lambda
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# lambda = function written in 1 line using lambda keyword.
# Accepts any number of arguments (parameters), but only has one epxression.
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)

# lambda parameters:expression

def double(x):
    return x * 2
print(double(5))
# this is the same as above lines of code.
double = lambda x:x*2
multiply = lambda x,y:x*y
add = lambda x,y,z: x+y+z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(5,6))
print(add(5,6,7))
print(full_name("Bro", "Code"))
print(age_check(18))
