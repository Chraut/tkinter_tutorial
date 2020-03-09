'''
Created on Mar 9, 2020

@author: marbe
'''
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Main Window")
root.iconbitmap('suez_logo.ico')

def open():
    global my_img
    top = Toplevel()
    top.title("New Window")
    top.iconbitmap('suez_logo.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/cat02.jpg"))
    my_label = Label(top, image= my_img).pack()  
    btn2 = Button(top, text="close window", command = top.destroy).pack()

btn = Button(root, text="Open Second Window", command = open).pack()


root.mainloop()  