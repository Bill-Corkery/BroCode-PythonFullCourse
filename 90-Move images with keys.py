#Lesson 90: Move image with keys
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind('<w>', move_up)
window.bind('<s>', move_down)
window.bind('<a>', move_left)
window.bind('<d>', move_right)

myimage = PhotoImage(file='racecar.png')
label = Label(window,image=myimage)
label.place(x=0,y=0)

window.mainloop()