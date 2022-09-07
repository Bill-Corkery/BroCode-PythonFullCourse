#Lesson 79:Save a File
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir='C://Users//WilliamBillCorkery//PycharmProjects//BroCode-PythonFullCourse',
                                    defaultextension='.txt',
                                    filetypes=[('Text File', '.txt'),
                                               ('HTML file', '.html'),
                                               ('All files', '.*')])
    if file is None:
        return # this is a way to make sure no error.
    file_text = str(text.get(1.0,END))
    # file_text = input("Enter some text I guess: ") #This is good but can do below if want to enter text via console
    file.write(file_text)
    file.close()

window = Tk()
button = Button(text="save", command=save_file)
button.pack()
text = Text(window)
text.pack()
window.mainloop()