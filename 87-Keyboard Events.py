#Lesson 87: Keyboard Events
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import  *

def doSomething(event):
    print("You pressed:" + event.keysym)
    label.config(text=event.keysym)

window = Tk()

# return is enter. Key is any key.
window.bind("<Return>", doSomething)
window.bind("<Key>", doSomething)

label = Label(window,font=('Helvetica', 100))
label.pack()

window.mainloop()