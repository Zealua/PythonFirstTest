import tkinter
from tkinter import*
from tkinter import messagebox

from driver import comPort

import time
import os

def newButtonBar(root,text2):
    global frame1
    global lable
    global TEXT2
    TEXT2=text2

    frame1=Frame(root,bg='red',bd=20, width = 350 )
    button1=Button(frame1,text=u'Calibrate', command=calibrate)
    button2=Button(frame1,text=u'Get dimensions', command=getParam)
    button3=Button(frame1,text=u'Send data to sever', command=Hello)

    lable=Label(frame1,text='COM OFF',width=8,height=1,bg='red',fg='green',font='arial 20') #bg='red',
    lable.pack(side='bottom')

    frame1.pack()
    button1.pack(side='left')
    button2.pack(side='left')
    button3.pack(side='left')

def setComOn():
    global frame1
    global lable
    frame1.config(bg='green')
    frame1.pack()
    lable.config(bg='green')
    frame1.pack()

def setComOf():
    global frame1
    global lable
    frame1.config(bg='red')
    frame1.pack()
    lable.config(bg='red')
    frame1.pack()

def Hello():
    print('Send data to server')
    messagebox.showinfo("Allert", "Send data to server")

def getParam():
    messagebox.showinfo("Allert", "Put item on scale, and press OK")
    comPort.write('-g'.encode());
    time.sleep(3)
    textT=comPort.read();
    print(textT)
    if textT is None:
        print('text -null')
    else:
        textT=textT[11:-1];
        print(textT)
        textTe5 = textT.replace('\\r',''); # textTe4
        global textTemp
        textTemp = textTe5.replace('\\n','');
        print(textTemp)
        TEXT2.configure(state=tkinter.NORMAL)
        TEXT2.insert(1.0,textTemp+"\n")
        TEXT2.configure(state=tkinter.DISABLED)

def calibrate():
    messagebox.showinfo("Allert", "Get all from Scales, and pess OK !!!")
    comPort.write('-c'.encode());
    time.sleep(3)
    textT=comPort.read();
    if textT is None:
        print('text -null')
    else:
        textT=textT[11:-1];
        print(textT)
        TEXT2.configure(state=tkinter.NORMAL)
        TEXT2.insert(1.0,textT+"\n")
        TEXT2.configure(state=tkinter.DISABLED)

def getDimension(event):
    messagebox.showinfo("Allert", "Put item on scale, and press OK")
    barCode=text1.get('1.0', END);
    barCode=barCode[:-1]
    comPort.write('-g'.encode());
    time.sleep(3)
    textT=comPort.read();
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
    TEXT2.configure(state=tkinter.NORMAL)
    TEXT2.insert(1.0,barCode+textTemp+"\n")
    TEXT2.configure(state=tkinter.DISABLED)

