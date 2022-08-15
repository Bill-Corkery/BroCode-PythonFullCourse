#Lesson 34: Copy a File
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# copyfile() = copies contents of a file
# copy()     = copyfile(0 + persmission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)

import shutil  #good module to copy files.
shutil.copyfile('test.txt', 'copy.txt') #this function has both a source (src) and a destination (dst)
# if file is not in project folder, would need to list the file path.