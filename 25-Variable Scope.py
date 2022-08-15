#Lesson 25: Variable Scope
# The region that a variable is recognized
# A variable is only available from inside the region it is created.
# A global and locally scoped version of a variable can be created.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

name = "Bro" # global scope because global variable (available inside & outside functions)

def display_name():
    name = "Code" # local scope because local variable (available only inside this function)
    print(name)
# Will first use local variable first then Global full rule below for Python
# LEGB Rule. Local. Then Enclosing. Then Global. Then Built-in.
display_name()
print(name)