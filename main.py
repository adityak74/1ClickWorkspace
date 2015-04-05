#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
from Tkinter import *
def hello(event):
    print("Single Click, Button-l") 
def quit(event):                           
    print("Double Click, so let's stop") 
    import sys; sys.exit() 
def getPath(event):
	Lb1.insert(END,E1.get())
def printActivePath(event):
	print("Clicked")

import tkMessageBox

top = Tk()
top.title("1Click-Workspace Manager");

var = StringVar()
label = Label( top, text= 'Workspace Paths')
label.pack()

frame = Frame(top, relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=1)

#var.set("Workspace Paths")


widget = Button(frame, text='Edit Paths')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit) 

Lb1 = Listbox(frame,selectmode = SINGLE)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.bind("<Button-1>", printActivePath)
Lb1.pack()

frame2 = Frame(top, relief=RAISED, borderwidth=1)
frame2.pack(fill=BOTH, expand=1)


v = StringVar()
L1 = Label(frame2, text="Enter Path")
L1.pack( side = LEFT)
E1 = Entry(frame2, bd =5 , textvariable =v)
E1.pack(side = RIGHT)

b2 = Button(top, text='Add Path')
b2.pack(side = RIGHT)
b2.bind('<Button-1>', getPath)

top.mainloop()