'''
Created on Mar 7, 2020

@author: marbe
'''
from tkinter import *

# we need to install PIL first -> check out video (at 1.22h)
# https://www.youtube.com/watch?v=YXPyB4XeYLA
# pip install Pillow

# check which packages are already installed
# pip freeze
from PIL import ImageTk, Image

root = Tk()
root.title("Icon Images")

# add icon -> .ico file
root.iconbitmap('C:/Users/marbe/Desktop/Projects/01 - Tutorial/tkinterTutorial/suez_logo.ico')


# add image
my_img = ImageTk.PhotoImage(Image.open("mountain.png"))
# when the image is in the same folder the path is not needed
my_label = Label(image=my_img)
my_label.grid(row=0,column=0)


# exit button
button_quite = Button(root, text="Exit Program", command= root.quit)
button_quite.grid(row=1,column=1)

root.mainloop()
