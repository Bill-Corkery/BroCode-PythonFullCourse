#Lesson 55: Sort
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# sort() method = used with lists
# sort() function = used with iterables

#this is sorting simple lists, tuples, etc.
students_0 = ("Squidward", "Sandy","Patrick","Spongebob","Mr. Krabs")
sorted_students_0 = sorted(students_0)
for i in sorted_students_0:
    print(i)

#this is for sorting complex things like list of tuples below.
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

students.sort() # can have students.sort(key=age) which will just sort by students age
for i in students:
    print(i)

age = lambda ages:ages[2]
students.sort(key=age) # can have students.sort(key=age) which will just sort by students age
for i in students:
    print(i)

#sort doesnt work well with tuples. so can use sorted() function with tuples.
grade = lambda grades:grades[1]
sorted_stuents = sorted(students, key=grade, reverse=True) # this reverses it
for i in sorted_stuents:
    print(i)