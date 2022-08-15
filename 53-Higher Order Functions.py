#Lesson 53: Higher Order Function
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# Higher Order Functions = a function that either:
# 1. accepts a function as an argument or
# 2. returns a function (In Python, functions are also treated as objects)

# example of a function as argument. loud and quiet go into hello as function arguments.
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

# example of a returning a function
def divisor(x):
    def dividend(y):
        return y/x
    return dividend
divide = divisor(2)
print(divide(10))
