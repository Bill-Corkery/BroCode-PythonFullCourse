#Lesson 66: Labels
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# labels = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo =PhotoImage(file='person.png')

#simple way to have a label.
#label = Label(window, text='Hello World')
#label.place(x=0,y=0) # this will place the label in a certain position

label = Label(window,
              text = 'Bro, do you even code?',
              font = ('Arial', 40, 'bold'),
              fg = '#00FF00',
              bg = 'black',
              relief = RAISED,
              bd = 10,
              padx = 20,
              pady=20,
              image = photo,
              compound="bottom")
label.pack()

window.mainloop()