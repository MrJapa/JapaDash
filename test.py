from tkinter import *
from tkvideo import tkvideo
import os
from os import path
os.chdir(os.path.dirname(os.path.abspath(__file__)))

root = Tk()
root.overrideredirect(1)
root.geometry("500x500+710+290")
my_label = Label(root,bd=0,highlightthickness=0)
my_label.pack()
player = tkvideo("images/loading.avi", my_label, loop = 1, size = (500,500))
player.play()

root.mainloop()