import tkinter
from tkinter import*
import time
import os

def newButtonBar(root):
    def Hello(event):
        print('Send data to server')
        messagebox.showinfo("Allert", "Send data to server")

    def getParam(event):
        messagebox.showinfo("Allert", "Put item on scale, and press OK")
        #print('get dimension')
        comPort.write('-g'.encode());
        time.sleep(3)
        textT=comPort.read();
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
        comPort.write('-c'.encode());
        time.sleep(3)
        textT=comPort.read();
        textT=textT[11:-1];
        print(textT)
        text2.configure(state=tkinter.NORMAL)
        text2.insert(1.0,textT+"\n")
        text2.configure(state=tkinter.DISABLED)

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
        text2.configure(state=tkinter.NORMAL)
        text2.insert(1.0,barCode+textTemp+"\n")
        text2.configure(state=tkinter.DISABLED)


    frame1=Frame(root,bg='green',bd=15, width = 300 )
    button1=Button(frame1,text=u'Calibrate')
    button2=Button(frame1,text=u'Get dimensions')
    button3=Button(frame1,text=u'Send data to sever')

    button1.bind("<Button-1>", calibrate)
    button2.bind("<Button-1>", getParam)
    button3.bind("<Button-1>", Hello)

    frame1.pack()
    button1.pack(side='left')
    button2.pack(side='left')
    button3.pack(side='left')