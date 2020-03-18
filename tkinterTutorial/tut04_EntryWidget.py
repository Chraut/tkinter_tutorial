'''
Created on Mar 7, 2020

@author: marbe
'''
from tkinter import *

root = Tk()

# Entry widget
#e = Entry(root, width=50, bg="blue", fg="white")    # bg color, text color
#e = Entry(root, borderwidth=5)                      # border size 
e = Entry(root)
e.pack()
e.insert(0,"Enter Your Name: ")

# Click callback
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

# create button
myButton = Button(root, text="Enter your name", command = myClick)
myButton.pack()

print(help(Button))

root.mainloop()