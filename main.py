#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
from multi_os_base import *
from Tkinter import *
def getPath(event):
	Lb1.insert(END,E1.get())

def deleteActivePath(event):
	Lb1.delete(ACTIVE)

def openActivePath(event):
	try:
		print(Lb1.get(ACTIVE))
		openFolder(Lb1.get(ACTIVE))
	except Exception, e:
		raise e
	


import tkMessageBox

top = Tk()
top.title("1Click-Workspace Manager");
top.minsize(width=400,height=400)

var = StringVar()
label = Label( top, text= 'Workspace Paths')
label.pack()

frame = Frame(top, relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=1)

#var.set("Workspace Paths")


editBt = Button(frame, text='Delete Path')
editBt.pack()
editBt.bind('<Button-1>', deleteActivePath)

Lb1 = Listbox(frame,selectmode = SINGLE)
Lb1.pack()

b2 = Button(frame, text='Open')
b2.pack(side = RIGHT)
b2.bind('<Button-1>', openActivePath)


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