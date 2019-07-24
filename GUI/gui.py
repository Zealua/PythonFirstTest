import argparse
import time
import serial
import os
TTY_DEVICE = "COM"
COM = 16;
#-----------------------------------------------

#------------------------------------------------
import tkinter
from tkinter import*
from tkinter import messagebox
root=Tk()

root.title(u'Dimensions and weight')
root.geometry("380x360")

def hello():
    print ("hello!")

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

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)
# display the menu
root.config(menu=menubar)

def Hello(event):
    print('Send data to server')
    messagebox.showinfo("Allert", "Send data to server")

def getParam(event):
    messagebox.showinfo("Allert", "Put item on scale, and press OK")
    #print('get dimension')
    s.write('-g'.encode());
    time.sleep(3)
    textT=str(s.read(s.inWaiting()));
    print(textT)
    textT=textT[11:-1];
    print(textT)
    # textTe1 = textT.replace('Weight:','');
    # textTe2 = textTe1.replace('Length:','');
    # textTe3 = textTe2.replace('Width:','');
    # textTe4 = textTe3.replace('Height:','');
    textTe5 = textT.replace('\\r',''); # textTe4
    global textTemp
    textTemp = textTe5.replace('\\n','');
    print(textTemp)
    text2.configure(state=tkinter.NORMAL)
    text2.insert(1.0,textTemp+"\n")
    text2.configure(state=tkinter.DISABLED)

def calibrate(event):
    messagebox.showinfo("Allert", "Get all from Scales, and pess OK !!!")
    s.write('-c'.encode());
    time.sleep(3)
    textT=str(s.read(s.inWaiting()));
    textT=textT[11:-1];
    print(textT)
    text2.configure(state=tkinter.NORMAL)
    text2.insert(1.0,textT+"\n")
    text2.configure(state=tkinter.DISABLED)

def getDimension(event):
    messagebox.showinfo("Allert", "Put item on scale, and press OK")
    barCode=text1.get('1.0', END);
    barCode=barCode[:-1]
    s.write('-g'.encode());
    time.sleep(3)
    textT=str(s.read(s.inWaiting()));
    print(textT)
    textT=textT[11:-1];
    print(textT)
    textTe1 = textT.replace('Weight:','');
    textTe2 = textTe1.replace('Length:','');
    textTe3 = textTe2.replace('Width:','');
    textTe4 = textTe3.replace('Height:','');
    textTe5 = textTe4.replace('\\r','');
    global textTemp
    textTemp = textTe5.replace('\\n','');
    print(barCode+textTemp);
    text1.delete('1.0', END)
    file.writelines(barCode+';'+textTemp+'\n');
    text2.configure(state=tkinter.NORMAL)
    text2.insert(1.0,barCode+textTemp+"\n")
    text2.configure(state=tkinter.DISABLED)

def com1():
    trySerial(1);
def com2():
    trySerial(2);
def com3():
    trySerial(3);
def com0():
    trySerial(0);
def com4():
    trySerial(4);
def com5():
    trySerial(5);
def com6():
    trySerial(6);
def com7():
    trySerial(7);
def com8():
    trySerial(8);
def com9():
    trySerial(9);
def com10():
    trySerial(10);
def com11():
    trySerial(11);
def com12():
    trySerial(12);
def com13():
    trySerial(13);
def com14():
    trySerial(14);
def com15():
    trySerial(15);
def com16():
    trySerial(16);
def com17():
    trySerial(17);
def com18():
    trySerial(18);



def trySerial(com):
    global s
    s.close();
    print('Serial close')
    try:
        s = serial.Serial(TTY_DEVICE + str(com), 115200, timeout=10)
        text2.configure(state=tkinter.NORMAL)
        text2.insert(1.0,'Serial open COM'+str(com)+"\n")
        text2.configure(state=tkinter.DISABLED)
        print('Serial open COM'+str(com))
    except (OSError, serial.SerialException):
        text2.configure(state=tkinter.NORMAL)
        text2.insert(1.0,"Try other COM port\n")
        text2.configure(state=tkinter.DISABLED)
        print('Try other COM port')
    
textTemp='';
s = serial.Serial(TTY_DEVICE + str(COM), 115200, timeout=10)
time.sleep(2) 

newpath = time.strftime('%Y%m%d');   #'C:\\temp\\'+ 
if not os.path.exists(newpath):
    os.makedirs(newpath);
fileName=newpath+'\\'+time.strftime('%H%M%S')+'.csv';
file=open(fileName,'a');
file.writelines('Part code; weight;  Length; Width; Height\n'); 


frame1=Frame(root,bg='green',bd=15, width = 300 )
button1=Button(frame1,text=u'Calibrate')
button2=Button(frame1,text=u'Get dimensions')
button3=Button(frame1,text=u'Send data to sever')

mb=  Menubutton ( root , text="Choose COM", relief=RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu

mb.menu.add_checkbutton ( label="COM0", command=com0)
mb.menu.add_checkbutton ( label="COM1", command=com1)
mb.menu.add_checkbutton ( label="COM2", command=com2)
mb.menu.add_checkbutton ( label="COM3", command=com3)
mb.menu.add_checkbutton ( label="COM4", command=com4)
mb.menu.add_checkbutton ( label="COM5", command=com5)
mb.menu.add_checkbutton ( label="COM6", command=com6)
mb.menu.add_checkbutton ( label="COM7", command=com7)
mb.menu.add_checkbutton ( label="COM8", command=com8)
mb.menu.add_checkbutton ( label="COM9", command=com9)
mb.menu.add_checkbutton ( label="COM10", command=com10)
mb.menu.add_checkbutton ( label="COM11", command=com11)
mb.menu.add_checkbutton ( label="COM12", command=com12)
mb.menu.add_checkbutton ( label="COM13", command=com13)
mb.menu.add_checkbutton ( label="COM14", command=com14)
mb.menu.add_checkbutton ( label="COM15", command=com15)
mb.menu.add_checkbutton ( label="COM16", command=com16)
mb.menu.add_checkbutton ( label="COM17", command=com17)
mb.menu.add_checkbutton ( label="COM18", command=com18)


button1.bind("<Button-1>", calibrate)
button2.bind("<Button-1>", getParam)
button3.bind("<Button-1>", Hello)
text1=Text(root,height=1,width=15,font='Arial 14',wrap=WORD)
text2=Text(root,height=15,width=50,font='Arial 10')
text2.configure(state=tkinter.DISABLED)
text1.bind("<Return>", getDimension)

text1.focus_set()
mb.pack(side='bottom')
frame1.pack()
button1.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')
text2.pack(side='bottom')
text1.pack(side='bottom')

root.mainloop()

