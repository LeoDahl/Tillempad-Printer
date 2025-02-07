## Code made by Leo Dahl
## Latest Change was made 2025-02-07 23:23

import serial.tools.list_ports
import time
import math


PortCom = 5 ## What port to use

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()


portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort)) ## Get all ports and print them out


serialInst.baudrate = 9600 ## Enter baudrate
serialInst.port = "COM"+str(PortCom) ## Define port
serialInst.open() ## Open port



def RunCommand(command, Xtime, YTime):
    print(command)
    serialInst.write(command.encode('utf-8'))
    if command == 'exit':
        exit()
    time.sleep(15)

