'''
Created on Mar 9, 2020

@author: marbe
'''
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Dropdown Menu")
root.iconbitmap('suez_logo.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root,text=clicked.get()).pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show selection", command=show)
myButton.pack()

root.mainloop()  