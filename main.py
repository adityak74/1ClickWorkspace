#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
from multi_os_base import *
from directoryListHandler import *
from fileHandler import *
from Tkinter import *
def hello():
    tkMessageBox.showinfo("Say Hello", "Hello World")
def showAbout():
    tkMessageBox.showinfo("About", "1-Click Workspace Manager\nVersion 0.1-beta\n\nDeveloped by Aditya Karnam\nTwitter : @akarnam37\nEmail:akarnam37@gmail.com\nFacebook:fb.com/adityakarnam.g")
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
def getWorkingList():
    list = Lb1.get(0, END)
    saveWorkspaceList(list)
    print list
def setWorkingList():
    workspaceList = loadWorkingList()
    if workspaceList is -1:
        print "No Save File"
        tkMessageBox.showinfo("Error", "No save file.Please save the list before you exit the program")
    else:
        workspaceList = workspaceList[::-1]
        Lb1.delete(0,END)
        for item in workspaceList:
            Lb1.insert( 0, item)



import tkMessageBox

top = Tk()
top.title("1Click-Workspace Manager")
top.minsize(width=400,height=400)

menubar = Menu(top)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=setWorkingList)
filemenu.add_command(label="Save", command=getWorkingList)
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
helpmenu.add_command(label="About", command=showAbout)
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

b2 = Button(frame2, text='Add Path')
b2.pack(side = RIGHT)
b2.bind('<Button-1>', getPath)

E1 = Entry(frame2, bd =5 , textvariable =v)
E1.pack(side = RIGHT)


top.mainloop()
