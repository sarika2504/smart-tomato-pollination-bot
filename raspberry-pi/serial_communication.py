import serial
from config import *

class Arduino:
    def __init__(self):
        self.arduino=serial.Serial(SERIAL_PORT,BAUD_RATE,timeout=1)

    def send(self,command):
        self.arduino.write(command.encode())

    def forward(self):
        self.send(FORWARD)

    def backward(self):
        self.send(BACKWARD)

    def left(self):
        self.send(LEFT)

    def right(self):
        self.send(RIGHT)

    def stop(self):
        self.send(STOP)

    def pollinate(self):
        self.send(POLLINATE)

if __name__=="__main__":
    bot=Arduino()
    while True:
        cmd=input("Command(F/B/L/R/S/P): ").upper()
        if cmd=="Q":
            break
        bot.send(cmd)
