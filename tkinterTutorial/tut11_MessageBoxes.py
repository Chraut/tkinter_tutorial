'''
Created on Mar 9, 2020

@author: marbe
'''
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap('suez_logo.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.showinfo(title="This is my popup!", message="Hello World!")
    Label(root, text=response).pack()
    
    #if response ==1:
    #    Label(root, text="You Clicked Yes!").pack()
    #else:
    #    Label(root, text="You Clicked No!").pack()
        
Button(root, text="Popup", command=popup).pack()


root.mainloop()  