#Lesson 81: Frames
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

#button = Button(window,text='W', font=('Consolas', 25), width=3)
#button.pack()

frame = Frame(window, bg='pink', bd=5,relief=RAISED)
#frame.pack(BOTTOM) #place below this replaces this function.
frame.place(x=0,y=0)


Button(frame,text='W', font=('Consolas', 25), width=3).pack(side=TOP)
Button(frame,text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame,text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame,text='D', font=('Consolas', 25), width=3).pack(side=LEFT)

window.mainloop()