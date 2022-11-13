import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setwarnings(False)

try:
        text = input('Password:')
        print("Tap NFC device")
        #reader.write(text)
        #id, text_in = reader.write_no_block(text)
        id, text_in = reader.write()
        print("Success")
finally:
        GPIO.cleanup()




