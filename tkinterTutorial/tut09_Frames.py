'''
Created on Mar 9, 2020

@author: marbe
'''
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")
root.iconbitmap('suez_logo.ico')

# here padx/Y is the inside space
frame = LabelFrame(root, text="This is my frame...", padx=50,pady=50)
# here padx/y is the outsite space
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="Don't Click Here!")
b.grid(row = 0, column=0)
b2.grid(row = 1, column=1)

root.mainloop()