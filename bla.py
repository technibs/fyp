import os
import re
import signal
import time
import random
import serial
val=0
test=-1
fh=open("processid.txt","r")
processId=int(fh.read())
fh.close()
while True:
    ser = serial.Serial("/dev/ttyUSB0", 9600)
    textln = ser.readline()
    textln=re.sub(r"[^\d]","",textln)
    val=int(textln)
    if val==test:
        print("Same",val)
    elif val == 1:
        test=val
        val=0
        os.kill(processId,signal.SIGUSR1)
        print("In site 1")
    elif val == 2:
        test=val
        val=0
        os.kill(processId,signal.SIGUSR2)
        print("In site 2")
    else:
        print("In site none")
		
		


