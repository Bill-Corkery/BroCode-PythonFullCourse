#Lesson 71: Checkbox
# https://www.youtube.com/watch?v=xiUTqnI6xk8

from tkinter import *

def display():
    if(x.get()==1):
        print("You agree!")
    else:
        print("You do not agree")

window = Tk()
x = IntVar()  #returns 1 or 0
python_photo = PhotoImage(file= 'Python Image.png')

check_button= Checkbutton(window,
                          text='I agree to something',
                          variable=x,
                          onvalue=1,
                          offvalue=0,
                          command = display,
                          font=('Arial', 20),
                          foreground='#00FF00',
                          background="black",
                          activeforeground='#00FF00',
                          activebackground = "black",
                          padx=25,
                          pady=10,
                          image=python_photo,
                          compound='left')

check_button.pack()
window.mainloop()