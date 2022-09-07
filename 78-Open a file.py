#Lesson 78: Open a file
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from tkinter import filedialog

def open_File():
    filepath = filedialog.askopenfilename(initialdir='C://Users//WilliamBillCorkery//PycharmProjects//BroCode-PythonFullCourse',
                                          title="Open File Please",
                                          filetypes=(('text files','*.txt'),
                                          ('all files', '*.*')))
    file = open(filepath,'r')
    print(file.read())
    print(filepath)
    file.close()

window = Tk()
button = Button(text="Open", command=open_File())
button.pack()
window.mainloop()