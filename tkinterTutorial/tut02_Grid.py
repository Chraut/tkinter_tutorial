'''
Created on Mar 7, 2020

@author: marbe
'''
from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel1 = Label(root, text="Hello world")
myLabel2 = Label(root, text="My name is Martin")
myLabel3 = Label(root, text="      ").grid(row=1,column=2)
# Shoving it onto the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)


root.mainloop()