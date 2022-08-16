#Lesson 65:Daemon Thread
# https://www.youtube.com/watch?v=XKHEtdqhLK8

# daemon thread = a thread that runs in the background, not important for program to run
#               your program will not wait for daemon threads to complete before exiting
#               non-daemon threads cannot normally be killed, stay alive until task is complete
#
#               Daemon thread examples: background tasks, garbage collection, waiting for input, long running processes

import threading
import time
def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")

# if dont change it to daemon thread, will continue
# x = threading.Thread(target=timer)
x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you wish to exit?")

# this is a way to set daemon thread to true or false
# x.setDaemon(True)
# this returns true of false
# print(x.isDaemon())