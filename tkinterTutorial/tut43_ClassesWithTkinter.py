'''
Created on Mar 17, 2020

@author: marbe
'''
from tkinter import *

root = Tk()
root.title("Classes with Tkinter")
root.iconbitmap('suez_logo.ico')
root.geometry("400x400")

class Elder:
    
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()
        
        self.myButton = Button(master, text="Click Me!", command=self.clicker)
        self.myButton.pack(pady=20)
    
    def clicker(self):
        print("Look at you... you clicked a button!")

e = Elder(root)
        
root.mainloop()