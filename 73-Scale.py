#Lesson 73: Scale
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()
#below adds image to the scale. 
#hotImage = PhotoImage(file = 'hot.png')
#hotLabel = Label(image=hotImage)
#hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font = ('Consolas',20),
              tickinterval = 10, #this adds numeric indicators for value
              showvalue = 0,   #hides current value
              troughcolor = 'blue',
              fg = '#FF1C00',
              bg = 'black')
#scale.set(100)   # this sets default slider. below sets it to the middle.
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(window,text='submit', command=submit)
button.pack()

window.mainloop()
