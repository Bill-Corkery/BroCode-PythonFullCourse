#Lesson 79: Color chooser
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from tkinter import colorchooser  #submodule. not necessary.

def click():
#    window.config(bg=colorchooser.askcolor()[1])  #one line of code version of below.
    color = colorchooser.askcolor() #assign color to a variable
    color_Hex = color[1]            #assigns element at index 1 to a varaible
    window.config(bg=color_Hex)     #change background color

window = Tk()
window.geometry('420x420')
button = Button(text='click me', command=click)
button.pack()
window.mainloop()