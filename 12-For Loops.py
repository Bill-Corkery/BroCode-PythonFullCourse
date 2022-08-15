#Lesson 12: For Loops
# a statement that will execute its block of code a limited
# amount of times.
# https://www.youtube.com/watch?v=XKHEtdqhLK8
import time

#i means index.
# The +1 will make the count 1 to 10 because starts at 0.
# Can also add the +1 to the range
#for i in range(10):
    #print(i+1)

#this program counts by 2
#for i in range(50,100+1,2):
    #print(i)

#for i in "Bro Code":
    #print(i)

#import time module at top of code.
# i can be anything. below it is seconds.
# the -1 it the step amount. so here it is counting down.
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")