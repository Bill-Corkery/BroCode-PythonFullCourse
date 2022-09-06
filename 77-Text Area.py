#Lesson 77: Text Area
# https://www.youtube.com/watch?v=xiUTqnI6xk8
# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Ink Free",16),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="blue")
text.pack()
button = Button(window,text="submit", command=submit)
button.pack()
window.mainloop()