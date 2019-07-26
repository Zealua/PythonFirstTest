import os
import time
import tkinter
from tkinter import*
from tkinter import messagebox

from buttonBar import buttonBar
from driver import comPort

first=1 
 
def newMenu(root,text2,file):
    def hello():
        print('it"s work')
    def sendServer():
        file.close()
    def About():
        messagebox.showinfo('About',"Програма для роботи з СКАНМАН\n\n     Zakaz.ua")
    def turnCom(com):
        comPort.init(com,text2)
        buttonBar.setComOn()

    def comDisconnect():
        comPort.disconnect(text2)
        buttonBar.setComOf()#root,text2);
    def openFolder():
        path=time.strftime('%Y%m%d');
        os.system(f'start {os.path.realpath(path)}')
    
    def findCom():
        comAvable=comPort.findCom()
        print(comAvable)
        menubar.delete(3)
        comMenu.delete(0,10)
        comMenu.add_command( label="Find COM", command=findCom)
        for i in comAvable:
            comMenu.add_command( label="COM"+str(i), command=lambda: turnCom(i))
        comMenu.add_command( label="Disconect", command=comDisconnect)  
        menubar.insert_cascade(3, label="COM", menu=comMenu)
        root.config(menu=menubar)
        global first
        if(first==0):
            buttonBar.setComOf()
        first=0

    # create a toplevel menu
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open folder", command=openFolder)
    filemenu.add_command(label="Send file to server", command=sendServer)
#    filemenu.add_command(label="Save", command=hello)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Calibrate", command=buttonBar.calibrate)
    editmenu.add_command(label="Get dimensions", command=buttonBar.getParam)
 #   editmenu.add_command(label="Paste", command=hello)
    menubar.add_cascade(label="Command", menu=editmenu)

    # COM menu
    comMenu = Menu(menubar, tearoff=0)
      
    menubar.add_cascade(label="COM", menu=comMenu)

    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=About)
    menubar.add_cascade(label="Help", menu=helpmenu)
    # display the menu
    root.config(menu=menubar)
    findCom();