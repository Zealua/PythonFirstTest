# this file PYTHON 3.7.3 for windows
# #!/usr/bin/python -u
import argparse
import time
import serial
import os
#import json

TTY_DEVICE = "COM"

def main(args):
    s = serial.Serial(TTY_DEVICE + str(args.device), 115200, timeout=10)
    time.sleep(2) 

    newpath = time.strftime('%Y%m%d');   #'C:\\temp\\'+ 
    if not os.path.exists(newpath):
        os.makedirs(newpath);
    fileName=newpath+'\\'+time.strftime('%H%M%S')+'.csv';
    file=open(fileName,'a');
    file.writelines('Part code; weight;  Length; Width; Height\n'); 

    while 1:
            print('Put command or barCode');
            text = input();
            if text=='-c':
                print('Remove all of the scales, and press ENTER');
                input();
                s.write(text.encode());
                time.sleep(3);
                barCode='';
            elif text=='Exit':
                print('Work Done. Data send server!');
                return
            else:
                print('Put the goods on the scales, and press ENTER');
                input();
                s.write('-g'.encode());
                time.sleep(3);
                barCode=text;
            textT=str(s.read(s.inWaiting()));
            textT=textT[10:-1];
            textTe1 = textT.replace('Weight:','');
            textTe2 = textTe1.replace('Length:','');
            textTe3 = textTe2.replace('Width:','');
            textTe4 = textTe3.replace('Height:','');
            textTe5 = textTe4.replace('\\r','');
            textTemp = textTe5.replace('\\n','');
            print(textTemp);
            #print(len(textTemp));
            if len(textTemp) >0:
                if textTemp[1]!='C':
                    file.writelines(barCode+';'+textTemp+'\n');   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MANAGE ENGINE')
    parser.add_argument('device', type=int,
                        help="number of ACM TTY device, COM<NUMBER>",
                        default=1)
    args = parser.parse_args()
    main(args)

    
