#Lesson 92: Multiple Animations
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from 92Ball import *   #or Ball
import time

window = Tk()
WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0,0,100,1,1,"white")
tennis_ball = Ball(canvas, 0,0,50,4,3,"yellow")
basket_ball = Ball(canvas, 0,0,125,8,7,"orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.02)

window.mainloop()