'''
Created on Mar 9, 2020

@author: marbe
'''
from tkinter import *
from PIL import ImageTk, Image
import numpy as np               # pip install numpy
import matplotlib.pyplot as plt  # pip install matplotlib

root = Tk()
root.title("Matplotlib")
root.iconbitmap('suez_logo.ico')
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    #plt.hist(house_prices, 50)
    plt.polar(house_prices)
    plt.show()

my_button = Button(root, text="Graph it!", command=graph)
my_button.pack()

root.mainloop()