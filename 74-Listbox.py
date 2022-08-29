#Lesson 74: Listbox
# https://www.youtube.com/watch?v=xiUTqnI6xk8
#listbox = a listing of slectable text items within its own container

from tkinter import *

window = Tk()
def submit():
    food=[]
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),EntryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
#    listbox.delete(listbox.curselection())  way to delete only one.
    listbox.config(height=listbox.size())

listbox=Listbox(window,
                bg='#f7ffde',
                font=("Constantia", 35),
                width=12,
                height=10,
                selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,'pizza')
listbox.insert(2,'pasta')
listbox.insert(3,'garlic bread')
listbox.insert(4,'soup')
listbox.insert(5,'salad')
listbox.config(height=listbox.size())

EntryBox = Entry(window)
EntryBox.pack()

SubmitButton = Button(window,text='submit', command=submit)
SubmitButton.pack()

AddButton = Button(window,text='add', command=add)
AddButton.pack()

DeleteButton = Button(window,text='delete', command=delete)
DeleteButton.pack()


window.mainloop()