#main part of the project
#either boolean the read.py
#read.py returns a string for easier comparing
#string1 == string1 == 1 scoop of food
#string1 != string 2 == 0 scoop of food
#string2 == string2 == 2 scoops of food
#then loop around
import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pw_1 = "onescoop"
pw_2 = "twoscoop"

servo_control_pin = 18
GPIO.setup(servo_control_pin, GPIO.OUT)

#frequency and dutycycle
pwm_freq = 100
forward = 20
backward = 10
co = 0

#activate the servo
pwm = GPIO.PWM(servo_control_pin, pwm_freq)

def check(text):
    global co

    if text == pw_1 :
        #print("1 scoop")
        pwm.start(forward)
        time.sleep(.3)
        pwm.ChangeDutyCycle(backward)
        time.sleep(3)
        co = 0

    if text == pw_2 :
        #print("2 scoop")
        pwm.start(forward)
        time.sleep(.6)        
        co = 0
    
    if text != pw_1 and text != pw_2:
        print("0 scoop")
        co = co + 1
        time.sleep(2)
    
    if co == 5:
       print("Cooldown...")
       co = 0
       time.sleep(30)
    #print("5 seconds")
    #time.sleep(5)
    print("ready...")

reader = SimpleMFRC522()

try:
        print("tap NFC Card")
        id, text = reader.read()
        print(id)
        print(text)
        pwm.start(0)

        while True:

                print("tap NFC Card")
                id, text = reader.read()
                print("NFC Password scanned is: " + text)
                check(text.strip())
                
finally:
        pwm.stop()
        GPIO.cleanup()

