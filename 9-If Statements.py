#Lesson 9: If Statements
#a block of code that will execute if it's condition is true
# https://www.youtube.com/watch?v=XKHEtdqhLK8

age = int(input("How old are you?:"))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age <0:
    print("You have not been born yet!")
else:
    print("You are a child!")
