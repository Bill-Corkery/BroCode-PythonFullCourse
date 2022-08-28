#Lesson 72: Radio Buttons
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# radio button = similar to checkbox, but you can only select one from a group
#I believe the pictures are too large so this isnt working.

from tkinter import *

food = ['pizza', 'hamburger', 'hotdog']

def order():
    if(x.get()==0):
        print('You ordered pizza!')
    elif(x.get()==1):
        print('You ordered a hotdog')
    elif(x.get()==2):
        print('You ordered a hamburger')
    else:
        print('huh?')

window = Tk()
Image_Pizza = PhotoImage(file='pizza.png')
Image_Hotdog = PhotoImage(file='Hotdog.png')
Image_Hamburger = PhotoImage(file='Hambuger.png')
Food_Images = [Image_Pizza, Image_Hamburger, Image_Hotdog]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share
                              value=index, #assigns each radiobutton a different value.
                              padx=25, #adds padding on x-axis
                              font=("Impact",50),
                              image=Food_Images[index], # this adds image to radio button
                              compound='left',   #adds image & text left side
                              indicatoron=0, #eliminate circle indicators
                              width=375,
                              command=order # this will set command of radio button to function.
                              )
    radiobutton.pack(anchor=W)

window.mainloop()