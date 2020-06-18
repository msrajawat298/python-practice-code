import serial
import time

class TextMessage:
        def __init__(self, recipient="9301123085", message="TextMessage.content not set."):
            self.recipient = recipient
            self.content = message

        def setRecipient(self, number):
            self.recipient = number

        def setContent(self, message):
            self.content = message

        def connectPhone(self):
            self.ser = serial.Serial('COM3',9600, timeout=5, xonxoff = False, rtscts = False,
            bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE)
            time.sleep(1)

        def sendMessage(self):
            self.ser.write('AT\r'.encode())
            time.sleep(2)
            self.ser.write('AT+CMGF=1\r'.encode())
            time.sleep(2)
            self.ser.write(('''AT+CMGS="''' + self.recipient + '''"\r''').encode())
            time.sleep(2)
            self.ser.write((self.content + "\r").encode())
            time.sleep(2)
            self.ser.write(chr(26).encode())
            time.sleep(3)
        def dialPhone(self):
            self.ser.write('AT\r'.encode())
            time.sleep(2)
            self.ser.write(('ATD'+self.recipient+';\r').encode())
            time.sleep(10)
        def disconnectPhone(self):
            self.ser.close()
sms = TextMessage("8223049561","Students i sent this message from my computer")
sms.connectPhone()
sms.sendMessage()
#sms.dialPhone()
sms.disconnectPhone()
print ("message sent successfully")



