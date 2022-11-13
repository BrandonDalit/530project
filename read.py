import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#GPIO.setwarnings(False)

reader = SimpleMFRC522()

try:
        print("tap NFC Card")
        #id, text = reader.read()
        id, text = self.read_no_block()
        print(id)
        print(text)
        
finally:
        GPIO.cleanup()






