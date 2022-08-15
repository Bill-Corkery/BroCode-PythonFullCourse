#Lesson 24: Nested Function Calls
# function calls inside other function calls
# innermost function calls are resolved first
# return value is used as arugment for the next outer function.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

num = input("Enter a whole positive number: ")
print(num)
num = float(num)
print(num)
num = abs(num)
print(num)
num = round(num)
print(num)
# this is a nested function call below. it combines all above functions.
print(round(abs(float(input("Enter a whole positive number: ")))))