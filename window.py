import numpy as np
import grid
from tkinter import *
from graphics import color_rgb
import setup
import defaultagent
import matrixgui
import customagent
val = 0
master = Tk()
Label(master,text="Dimension:",width = 20).grid(row = 0)
Label(master,text="Number of Mines:",width = 20).grid(row = 1)

e1 = Entry(master,width=20,bg="white")
e2 = Entry(master,width=20,bg="white")

e1.grid(row=0,column = 1)
e2.grid(row=1,column = 1)

def click():
    entered_text1 = e1.get()
    entered_text2 = e2.get()
    val = setup.setup(int(entered_text1),int(entered_text2))
    print(val)
    matrixgui.matrix_gui(int(entered_text1),val)

def default_agent():
    entered_text1 = e1.get()
    entered_text2 = e2.get()
    val = setup.setup(int(entered_text1),int(entered_text2))
    matrixgui.matrix_gui(int(entered_text1),val)
    defaultagent.start_agent(int(entered_text1),val)

def improved_agent():
    entered_text1 = e1.get()
    entered_text2 = e2.get()
    val = setup.setup(int(entered_text1),int(entered_text2))
    matrixgui.matrix_gui(int(entered_text1),val)
    customagent.start_agent(int(entered_text1),val)

def leave():
    exit()

Button(master,text="Show Board",command = click).grid(row=3,column=0,sticky=W,pady=4)
Button(master,text="Default Agent",command = default_agent).grid(row=3,column=1,sticky=W,pady=4)
Button(master,text="Improved Agent",command = improved_agent).grid(row=3,column=2,sticky=W,pady=4)
Button(master,text="Exit",command = leave).grid(row=3,column=3,sticky=W,pady=4)
master.mainloop()
mainloop()
