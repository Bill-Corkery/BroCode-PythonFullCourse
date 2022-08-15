#Lesson 17: Tuple
# a collection which is ordered and unchangeable. used to group together realted data
# https://www.youtube.com/watch?v=XKHEtdqhLK8

student = ("Bro", 21, "male")
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")