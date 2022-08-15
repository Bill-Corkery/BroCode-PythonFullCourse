#Lesson 58: Reduce
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# reduce()= apply a function to a iterable and reduce it to a single cumulative value.
# performs function on first tow elements and repeats process until 1 value remains.

# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x,y,:x+y, letters)
print(word)

factorial = [5,4,3,2,1]
results = functools.reduce(lambda x,y,:x*y, factorial)
print(results)