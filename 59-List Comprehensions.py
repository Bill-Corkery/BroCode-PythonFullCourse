#Lesson 59: List Comprehensions
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# list comprehension = a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable if conditional] <-- if one if condition
# list = [expression (if/else) for item in iterable]      <-- if have if/else condition

squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i*i)     # define what each loop iteration should do
print(squares)

squares1 = [i*i for i in range(1,11)]
print(squares1)

#using lambda
students = [100,90,80,70,60,50]
passed_students = list(filter(lambda x:x>=60, students))
print(passed_students)

#using list comprehension
passed_students1 = [i for i in students if i>=60]
passed_students2 = [i if i>=60 else "Failed" for i in students]
print(passed_students1)
print(passed_students2)
