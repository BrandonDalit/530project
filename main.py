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

x = True

#activate the servo
    pwm = GPIO.PWM(servo_control_pin, pwm_freq)

def check(text):
    if text == pw_1 :
        #print("1 scoop")
        pwm.start(forward)
        time.sleep(3)
        pwm.ChangeDutyCycle(backward)
        time.sleep(3)

    elif text == pw_2 :
        #print("2 scoop")
        pwm.start(forward)
        time.sleep(6)
        pwm.ChangeDutyCycle(backward)
        time.sleep(6)

    elif text != pw_1 and text != pw_2:
        print("0 scoop")
    print("5 seconds")
    time.sleep(5)
    print("ready...")

reader = SimpleMFRC522()

try:
        print("tap NFC Card")
        id, text = reader.read()
        print(id)
        print(text)

        while x:
                print("tap NFC Card")
                id, text = reader.read()
                print("NFC Password scanned is: " + text)
                check(text.strip())

finally:
        pwm.stop()
        GPIO.cleanup()
