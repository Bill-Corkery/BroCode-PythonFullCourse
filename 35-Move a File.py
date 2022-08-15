#Lesson 35: Move a file
# move a file from projects folder to desktops folder.
# https://www.youtube.com/watch?v=XKHEtdqhLK8

import os
source = "test.txt"
destination = "C:\\Users\\WilliamBillCorkery\\OneDrive - Iberia Advisory\\Desktop\\text.txt"

try: #recommend doing code in try/except block to handle issues.
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")