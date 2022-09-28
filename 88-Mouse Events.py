#Lesson 87: Keyboard Events
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def doSomething(event):
    # this shows where the mouse button was clicked on screen
    print("Mouse coordinates: "+str(event.x)+","+str(event.y))

window = Tk()

window.bind('<Button-1>', doSomething)  # left mouse button click
window.bind('<Button-2>', doSomething)  # mouse scroll wheel
window.bind('<Button-3>', doSomething)  # right mouse button click
window.bind('<ButtonRelease>', doSomething)  # shows where the button release happened
window.bind('<Enter>', doSomething)  # enter the window
window.bind('<Leave>', doSomething)  # leave the window
window.bind('<Motion>', doSomething)  # where the mouse moved

window.mainloop()