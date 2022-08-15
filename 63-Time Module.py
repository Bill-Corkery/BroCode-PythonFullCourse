#Lesson 63:Time Module
# https://www.youtube.com/watch?v=XKHEtdqhLK8
import time

print(time.ctime(0))    # convert a time expressed in seconds epoch to a readable string
                        # epoch = when your computer thinks time began (reference point)
print(time.time())  # return current seconds since epoch
print(time.ctime(time.time())) # will get current time.
time_object = time.localtime()
time_object = time.gmtime() # this is UTC time.
print(time_object)
local_time = time.strftime("%B %d %Y %H: %M:%S", time_object) # go to python offical documentation
print(local_time)

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y") # this parse a string a return time object.
print(time_object)

# asctime will accept tuple format.
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple) # accepts a tuple representation of time.
print(time_string)

# mktime will take time and convert it to seconds since epoch.
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple) # accepts a tuple representation of time.
print(time_string)