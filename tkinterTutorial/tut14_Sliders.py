'''
Created on Mar 9, 2020

@author: marbe
'''
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
root.iconbitmap('suez_logo.ico')
root.geometry("400x400")

vertical = Scale(root, from_=400, to=800)
vertical.pack()

def slide(var):
    my_label = Label(root, text = horicontal.get()).pack()
    root.geometry(str(horicontal.get())+"x"+str(vertical.get()))

horicontal = Scale(root, from_=400, to=800, orient=HORIZONTAL, command=slide)
horicontal.pack()

my_btn = Button(root, text="Click Me!",command=lambda: slide(1)).pack()

root.mainloop()  