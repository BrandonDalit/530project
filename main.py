#main part of the project 
#either boolean the read.py
#read.py returns a string for easier comparing
#string1 == string1 == 1 scoop of food
#string1 != string 2 == 0 scoop of food
#string2 == string2 == 2 scoops of food
#then loop around 

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)

pw_1 = "onescoop"
pw_2 = "twoscoop"

x = 0

reader = SimpleMFRC522()

try:
        print("tap NFC Card")
        id, text = reader.read()
        print(id)
        print(text)

        while x < 1 :
                print("tap NFC Card")
                id, text = reader.read()
                print(id)
                print(text)

        if text == pw_1:
                print("1 scoop")

        elif text == pw_2:
                print("2 scoop")

        else:
                print("0 scoop")

finally:
        GPIO.cleanup()
