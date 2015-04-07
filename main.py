#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
from multi_os_base import *
from fileHandler import *
from Tkinter import *
def hello():
    tkMessageBox.showinfo("Say Hello", "Hello World")
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

menubar = Menu(top)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=top.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
top.config(menu=menubar)

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