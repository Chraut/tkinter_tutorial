'''
Created on Mar 9, 2020

@author: marbe
'''
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open Files")
root.iconbitmap('suez_logo.ico')

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/marbe/Desktop/Projects/01 - Tutorial/tkinterTutorial/images", title="Select A File", filetypes=(("jpg files","*.jpg"),("png files","*.png"),("all files","*.*")))

    my_label = Label(root, text= root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_button = Button(root, text="Open File", command=open).pack()

root.mainloop()  