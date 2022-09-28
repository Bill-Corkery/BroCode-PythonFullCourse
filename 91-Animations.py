#Lesson 91: Animations
# https://www.youtube.com/watch?v=xiUTqnI6xk8
from tkinter import *
import time

WIDTH = 500     #make it upercase to show that it is constant (naming convention)
HEIGHT = 500
x_velocity = 3
y_velocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
#if want background photo. do this first so photo is in background
#background_image = PhotoImage(file='person.PNG')
#background = canvas.create_image(0,0,image=background_image,anchor = NW)

photo_image = PhotoImage(file='person.PNG')
my_image = canvas.create_image(0,0,image=photo_image,anchor = NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates) # useful for learning purposes
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        x_velocity = -x_velocity #this inverts direction
    if (coordinates[1] >=(HEIGHT - image_height) or coordinates[1] < 0):
        y_velocity = -y_velocity  # this inverts direction
    canvas.move(my_image,x_velocity,0)
    window.update()
    time.sleep(0.01)

window.mainloop()