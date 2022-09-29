#Lesson 93: Clock Program
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_time_string = strftime("%A")
    day_time_label.config(text=day_time_string)

    date_time_string = strftime("%B %d, %Y")
    date_time_label.config(text=date_time_string)

    window.after(1000,update)   #this is 1000 miliseconds. this is also recurisve as update is called.

window = Tk()

time_label = Label(window, font=("Arial", 50), fg="blue", bg="black")
time_label.pack()

day_time_label = Label(window, font=("Inke Free", 25))
day_time_label.pack()

date_time_label = Label(window, font=("Inke Free", 50))
date_time_label.pack()


update()

window.mainloop()