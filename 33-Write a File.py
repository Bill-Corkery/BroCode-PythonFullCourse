#Lesson 33: Write a File
#
# https://www.youtube.com/watch?v=XKHEtdqhLK8

text = "Hello \nThis is some text \nHave a good date!\n"# \n is a new line.
with open('test.txt', 'w') as file: #by default the mode is r. but here it is set to w for write.
    #mode 'a' will append the new lines to the file.
    file.write(text)