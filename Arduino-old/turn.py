# this file PYTHON 3.7.3 for windows
# #!/usr/bin/python -u
import argparse
import time
import serial

TTY_DEVICE = "COM"

def main(args):
    s = serial.Serial(TTY_DEVICE + str(args.device), 115200, timeout=10)
    time.sleep(2)    
    s.write("0".encode())
    data = (s.readline())
    s.write('%d\n'.encode() % args.direction)
    s.flushOutput();
    if "INTERRUPTED".encode() in data:
        print (data)
        s.close()
    #    raise
    
    data = s.readline()
    print (data)
    print (s.readline())

    s.write('%d\n'.encode() % args.speed)
    data = s.readline()
    if "INTERRUPTED".encode() in data:
        print (data)
        s.close()
    #    raise
    print (data)
    print (s.readline())

    s.write('%d\n'.encode() % args.angle)
    data = s.readline()
    if "INTERRUPTED".encode() in data:
        print (data)
        s.close()
    #    raise
    print ( data)
    print (s.readline())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MANAGE ENGINE')
    parser.add_argument('device', type=int,
                        help="number of ACM TTY device, COM<NUMBER>",
                        default=1)
    parser.add_argument('direction', type=int,
                        help='Engine turn direction: 1/2')
    parser.add_argument('speed', type=int,
                        help='Engine speed: 500-3500')
    parser.add_argument('angle', type=int,
                        help='Angle: 1-720')
    args = parser.parse_args()
    main(args)
