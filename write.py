import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

GPIO.setwarnings(False)

try:
        text = input('Password:')
        print("Tap NFC device")
        reader.write(text)
        print("Success")
finally:
        GPIO.cleanup()




