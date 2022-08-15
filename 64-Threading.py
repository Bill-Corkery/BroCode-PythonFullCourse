#Lesson 64:Threading
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# thread = a flow of execution, like a separate order of instructions.
#               However each thread takes a turn running to achieve concurrency
#               GIL = Global interpreter lock, allows only one thread to hold
#               control of the python interpreter at any one time

# CPU bound = program/task spends mos of its time waiting for internal events
#               (CPU intensive). Use multiprocessing.

# io bound = program/task spends most of its time waiting for external events
#               (user input, web scraping). use multithreading.

import threading
import time

# in the example below, lots of time will be IO bound as waiting for sleep
# so running on main thread see it takes 12 seconds.
def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finish studying")

#eat_breakfast()
#drink_coffee()
#study()
# these tasks were complete sequentailly.
#  but realistically we as humans these tasks can be completed together.
# so basically multithreading.

x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()
# this program only took 5 seconds as there were 4 threads running.
# these threads were run concurrently.
# active count and enumerate were called first as main thread called these first

# if want our main thread to wait for 3 instructive threads, use join below.
x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())  # trick to return how long calling thread/main
# thread to finish instructions. main thread is in charge of creating 3 additonal threads.

