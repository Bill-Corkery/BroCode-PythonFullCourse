#Lesson 31: File Detection
# https://www.youtube.com/watch?v=XKHEtdqhLK8

import os
path = "C:\\Users\\WilliamBillCorkery\\OneDrive - Iberia Advisory\\Desktop\\folder"
# need to manually put in double back slashes
if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location does not exist")