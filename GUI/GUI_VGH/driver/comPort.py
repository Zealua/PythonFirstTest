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
    
def write(text):
    global s
    s.write(text)

def read():
    global s 
    text=str(s.read(s.inWaiting()));
    return text
    
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