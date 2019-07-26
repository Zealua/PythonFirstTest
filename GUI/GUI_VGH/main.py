#import argparse
import time
import os
from menu import menu
from buttonBar import buttonBar
from driver import comPort
#------------------------------------------------
import tkinter
from tkinter import*
from tkinter import messagebox

root=Tk()
root.title(u'Dimensions and weight')
root.geometry("380x380")

textTemp='';

text2=Text(root,height=15,width=50,font='Arial 10')
text2.configure(state=tkinter.DISABLED)

newpath = time.strftime('%Y%m%d');   #'C:\\temp\\'+ 
if not os.path.exists(newpath):
    os.makedirs(newpath);
fileName=newpath+'\\'+time.strftime('%H%M%S')+'.csv';
file=open(fileName,'a');
file.writelines('Part code; weight;  Length; Width; Height\n'); 

menu.newMenu(root,text2,file);

def getDimension(event):
    messagebox.showinfo("Allert", "Put item on scale, and press OK")
    barCode=text1.get('1.0', END);
    barCode=barCode[:-1]
    comPort.write('-g'.encode());
    time.sleep(3)
    textT=comPort.read();
    if textT is None:
        print('text -null')
    else:
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
        try:
            file.writelines(barCode+';'+textTemp+'\n');
        except ValueError:
            print('error open file, re open')
            file=open(fileName,'a');
            file.writelines(barCode+';'+textTemp+'\n');
        text2.configure(state=tkinter.NORMAL)
        text2.insert(1.0,barCode+textTemp+"\n")
        text2.configure(state=tkinter.DISABLED)

buttonBar.newButtonBar(root,text2)

text1=Text(root,height=1,width=15,font='Arial 14',wrap=WORD)
text1.bind("<Return>", getDimension)
text1.focus_set()

text2.pack(side='bottom')
text1.pack(side='bottom')

root.mainloop()

