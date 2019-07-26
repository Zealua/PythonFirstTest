import serial
import tkinter
from tkinter import*

TTY_DEVICE = "COM"

s=serial.Serial()

def init(port,text2):
    global s
    try:
        s=serial.Serial(TTY_DEVICE + str(port), 115200, timeout=10)
        print('connect com'+str(port))
        text2.configure(state=tkinter.NORMAL)
        text2.insert(1.0,'connect COM'+str(port)+"\n")
        text2.configure(state=tkinter.DISABLED)
    except (OSError, serial.SerialException):
        pass
    
def disconnect(text2):
    global s
    text2.configure(state=tkinter.NORMAL)
    text2.insert(1.0,'COM-port Disconnect'+"\n")
    text2.configure(state=tkinter.DISABLED)
    s.close();
    print('COM-port Disconnect')

def write(text):
    global s
    try:
        s.write(text)
    except serial.SerialException:
         print('com port disconnect')

def read():
    global s 
    try:
        text=str(s.read(s.inWaiting()));
        return text
    except serial.SerialException:
        print('com port disconnect')
    
def findCom():
    global s
    s.close()
    print('com close')
    comAvable=[]
    for i in range(0,50):
        try:
            s = serial.Serial(TTY_DEVICE + str(i), 115200, timeout=10)
            comAvable.append(i)
            s.close()
            print('Serial close')
        except (OSError, serial.SerialException):
            pass
    else:
        return comAvable