#Lesson 83: Window Tabs
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)  # widget that managed a collection of windows/displays

tab1=Frame(notebook)  #this will be new frame for tab 1
tab2=Frame(notebook)
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack(expand=True, fill='both')  #expand = expand to fill any space not used.
                                            # fill = fill space on x and y axis.

Label(tab1,text='Hello, this is tab #1', width=50, height=25).pack()
Label(tab2,text='Goodbye, this is tab #2', width=50, height=25).pack()

window.mainloop()