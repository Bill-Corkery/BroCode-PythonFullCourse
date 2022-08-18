#Lesson 70: Entrybox
# https://www.youtube.com/watch?v=xiUTqnI6xk8

#entry widet = textbox that accepts a single line of user input
from tkinter import *

def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)  # this makes it so unable to make changes once click submit.

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window, font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*")   #this is a good way to hide what user is writing, good with passwords. 
entry.insert(0,'Default Text')
entry.pack(side =LEFT)

submit_button = Button(window,text="submit", command=submit)
submit_button.pack(side = RIGHT)

delete_button = Button(window,text="delete", command=delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window,text="backspace", command=backspace)
backspace_button.pack(side = RIGHT)

window.mainloop()