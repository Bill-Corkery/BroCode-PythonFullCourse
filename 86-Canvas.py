#Lesson 86: Canvas
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# canvas = widget that is used to draw graphs, plots, images in a window.

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
#blueLine=canvas.create_line(0,0,500,500, fill='blue', width=5)  # can set this to a value
#redLine=canvas.create_line(0,500,500,0, fill='red', width=5) # notice this is overlaping blue line.
#canvas.create_rectangle(50,50,250,250, fill='purple')
#points = 250,0,500,500,0,500
#canvas.create_polygon(points, fill='yellow', outline='black', width=5)
#canvas.create_arc(0,0,500,500, fill='green', style=PIESLICE, start=180, extent=180)

#create a pokibal
canvas.create_arc(0,0,500,500, fill='red', extent=180, width=10)
canvas.create_arc(0,0,500,500, fill='white', extent=180,start=180, width=10)
canvas.create_oval(190,190,310,310, fill='white', width=10)
canvas.pack()

window.mainloop()
