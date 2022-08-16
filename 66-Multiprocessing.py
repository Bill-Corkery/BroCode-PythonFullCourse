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
# this way below with only is if dont have multiprocessing
#    a = Process(target= counter, args=(1000,))
#    a.start
#    a.join
    print(cpu_count())
    a = Process(target=counter, args=(500,))
    b = Process(target=counter, args=(500,))
    a.start()
    b.start()
    a.join()
    b.join()
    print("Finished in:", time.perf_counter(), "Seconds")

# for some reason, my results are seconds since something? I got 103233 while it should be ~15 seconds.
if __name__ == '__main__':
    main()