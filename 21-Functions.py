#Lesson 21: Function
# a block of code which is executed only when it is called.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# what is given (Bro) is argument (information sending to function).
# These match to parameters (first_name).
def hello(first_name, last_name, age):
    print("Hello "+first_name+" "+last_name)
    print("You are "+ str(age) + " years old") # need to convert int to str.
    print("Have a nice day!")

hello("Bro", "Code", 33)