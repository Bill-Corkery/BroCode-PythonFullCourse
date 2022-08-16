#Lesson 66: Multiprocessing
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# multiprocessing = running tasks in parallel on different cpu cores, bypassing GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy CPU usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    pass

if __name__ = '__main__':
    main()