#Lesson 61: Zip Function
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

username = ["Dude", "Bro", "Mister"]
passwords = ("passwprd", "abc123", "guest")
users = dict(zip(username, passwords))
# users = list(zip(username, passwords)) can also make this into a list zip.
print(type(users))

for i in users:
    print(i)

for key, value in users.items():
    print(key+" : "+value)