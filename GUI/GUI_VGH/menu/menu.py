import tkinter
from tkinter import*

from driver import comPort

 
def newMenu(root,text2):
    def hello():
        print ("hello!")
    def turnCom(com):
        comPort.init(com,text2)
    
    def findCom():
        comAvable=comPort.findCom()
        print(comAvable)
        menubar.delete(3)
        comMenu.delete(0,10)
        comMenu.add_command( label="Find COM", command=findCom)
        for i in comAvable:
            comMenu.add_command( label="COM"+str(i), command=lambda: turnCom(i))  
        menubar.insert_cascade(3, label="COM", menu=comMenu)
        root.config(menu=menubar)



    # create a toplevel menu
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=hello)
    filemenu.add_command(label="Save", command=hello)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=hello)
    editmenu.add_command(label="Copy", command=hello)
    editmenu.add_command(label="Paste", command=hello)
    menubar.add_cascade(label="Edit", menu=editmenu)

    # COM menu
    comMenu = Menu(menubar, tearoff=0)
      
    comMenu.add_command( label="Find COM", command=findCom)      
    comMenu.add_command( label="COM0", command=hello)
    menubar.add_cascade(label="COM", menu=comMenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=hello)
    menubar.add_cascade(label="Help", menu=helpmenu)
    # display the menu
    root.config(menu=menubar)
    findCom();