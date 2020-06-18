import serial
import time
class Mobile:
    def Configure(self,comPort):
        self.ser=serial.Serial(comPort,9600,timeout=5,xonxoff=False,rtscts=False,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE)

    def Dial(self,phone):
        self.ser.write("AT\r".encode());
        time.sleep(0.5)
        self.ser.write(("ATD"+phone+";\r").encode());
        time.sleep(1)

    def SendSms(self, phone,msg):
        self.ser.write("AT\r".encode());
        time.sleep(0.5)
        self.ser.write("AT+CMGF=1\r".encode());
        time.sleep(0.5)
        self.ser.write(("AT+CMGS=\"" + phone + "\"\r").encode());
        time.sleep(2)
        self.ser.write((msg+"\r").encode())
        time.sleep(2)
        self.ser.write(chr(26).encode())
        time.sleep(2)
    def ReadSms(self):
        self.ser.write("AT\r".encode());
        time.sleep(0.5)
        self.ser.write("AT+CMGF=1\r".encode());
        time.sleep(0.5)
        self.ser.write("AT+CNMI=1,2,0,0,0\r".encode());
        time.sleep(1)
        while True:
            data1=self.ser.readline()
            if(data1.__len__()>4):
             print(data1.decode())


M=Mobile();
M.Configure("COM10")
ph=input("Enter Phone Number:")
M.Dial(ph)

# M.SendSms("9301123085","Hello")
#M.ReadSms()
print("Press Any Key To Cont...")
input()




