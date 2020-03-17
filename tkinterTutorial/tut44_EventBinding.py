'''
Created on Mar 17, 2020

@author: marbe
'''
from tkinter import *

root = Tk()
root.title("Classes with Tkinter")
root.iconbitmap('suez_logo.ico')
root.geometry("400x400")

def clicker(event):
    # coordinates of the mouse
    #myLabel = Label(root, text="You clicked a button " + str(event.x) + " " + str(event.y))
    myLabel = Label(root, text="You clicked this button " + event.char)
    myLabel.pack()


myButton = Button(root, text="Click Me!")
# Button-1 = mouse left click, -2: middle, -3 right
#myButton.bind("<Button-3>", clicker)

# enter widget
#myButton.bind("<Enter>", clicker)

# leave widget
#myButton.bind("<Leave>", clicker)

myButton.bind("<Key>", clicker)
myButton.pack()

root.mainloop()