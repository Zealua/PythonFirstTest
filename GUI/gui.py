''' import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton

class SimpleExample1(BaseWidget):
    
    def __init__(self):
        super(SimpleExample1,self).__init__('Simple example 1')

        #Definition of the forms fields
        self._firstname  = ControlText('First name', 'Default value')
        self._middlename = ControlText('Middle name')
        self._lastname   = ControlText('Lastname name')
        self._fullname   = ControlText('Full name')
        self._button     = ControlButton('Press this button')

#Execute the application
if __name__ == "__main__": pyforms.start_app( SimpleExample1 ) '''

import tkinter
from tkinter import *
root = Tk();

root.title(u'Dimensions and weight')

def Hello(event):
    print( "Yet another hello world");


btn = Button(root,                  #родительское окно
             text="Say hi",       #надпись на кнопке
             width=300,height=50,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
#btn.pack()                          #расположить кнопку на главном окне
""" clbrt.pack()
wght.pack()
dmnsns.pack()
 """
Button(root, text = 'Calibrate').place(x = 15, y = 15, width = 70,height = 25);
Button(root, text = 'Get WEIGHT').place(x = 95, y = 15, width = 80,height = 25);
Button(root, text = 'Get dimensions').place(x = 180, y = 15, width = 100,height = 25);

root.mainloop()