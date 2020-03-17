'''
Created on Mar 10, 2020

@author: marbe
'''
# imports
from tkinter import *


# create tkinter object
root = Tk()


dropAcc = OptionMenu(root, "list1", "list2")

# returns attributes
print(dropAcc['menu'].keys())
