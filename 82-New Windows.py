#Lesson 82: New Window
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def window_create():
    # window_new = Toplevel() #this new window is dependent on main window.
    window_new = Tk() #this new window is not dependent on main window.
    window_old.destroy()  # this creates a new window and closes out of old window.

window_old = Tk()

Button(window_old,text='create new window', command=window_create).pack()

window_old.mainloop()