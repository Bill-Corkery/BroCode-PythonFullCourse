#Lesson 51: Walrus Operator :=
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# new to Python 3.8
# assignment expression aka walrus operator
# assigned values to variables as part of a lager expression

happy = True
print(happy)
print(happy := True) #in this walrus operator, happy is assigned to True and printed in same line

#example without walrus
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
#example with walrus
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)