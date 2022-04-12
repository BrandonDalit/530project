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

#global Variables
co = 0 #Counter
t1 = 3 #end 3 hrs but changed to 3 seconds to demo purpose
t2 = 2 #end 2 hrs but changed to 2 seconds to demo purpose
tb1 = 0 #Time beginning 
tb2 = 0 #Time beginning
te1 = 0 #Time End
te2 = 0 #Time End
tn1 = 0
tn2 = 0
flag1 = False
flag2 = False


#activate the servo
pwm = GPIO.PWM(servo_control_pin, pwm_freq)

def timer(text):
    global tb1, tb2, te1, te2, tn1, tn2
    now = time.time()
    
    #Starts to add the delay for pw_1
    if text == pw_1 and flag1 == True:
        tn1 = now
        tb1 = now
        te1 = tb1 + t1
    
    #Starts to add the delay for pw_2
    elif text == pw_2 and flag2 == True:
        tn2 = now
        tb2 = now
        te2 = tb2 + t2
        
    else:
        tn1 = now
        tn2 = now
    #print("tn1: " + time.ctime(tn1) + " tn2: " + time.ctime(tn2) + "\ntb1: " + time.ctime(tb1) + " tb2: " + time.ctime(tb2) + "\nte1: " + time.ctime(te1) + " te2: " + ti>
        
def timout():
    global tb1, te2, flag1, flag2, tn1, tn2 
    tn1 = time.time()
    tn2 = time.time()
    if tn1 < te1:
        flag1 = False
    
    if tn2 < te2:
        flag2 = False

    if tn1 >= te1:
        flag1 = True
        

    if tn2 >= te2:
        flag2 = True
    #print("fg1: " + str(flag1) + ", fg2: " + str(flag2)) 
    #print("tn1: " + time.ctime(tn1) + " tn2: " + time.ctime(tn2) + "\nte1: " + time.ctime(te1) + " te2: " + time.ctime(te2))

def check(text):
    global co

    if text == pw_1 :
        #print("1 scoop")
        pwm.start(forward)
        time.sleep(.3)
        pwm.ChangeDutyCycle(backward)
        #time.sleep(3)
        co = 0

    if text == pw_2 :
        #print("2 scoop")
        pwm.start(forward)
        time.sleep(.6)        
        pwm.ChangeDutyCycle(backward)
        co = 0
    
    if text != pw_1 and text != pw_2:
        print("0 scoop")
        co = co + 1
        #time.sleep(2)
    
    if co == 5:
       print("Cooldown...")
       co = 0
       time.sleep(30)
    #print("5 seconds")
    #time.sleep(5)
    print("ready...\n")

reader = SimpleMFRC522()

try:
        #print("tap NFC Card")
        id, text = reader.read()
        #print(id)
        #print(text)
        pwm.start(0)

        while True:

                print("tap NFC Card")
                id, text = reader.read()
                print("NFC Password scanned is: " + text)
                
                if text.strip() == pw_1:
                    timout()
                    timer(pw_1)
                    if tb1 == tn1 and flag1 == True:
                        print("Time started: " + time.ctime(tn1) + ", timeout will halt after " + time.ctime(tb1 + t1) + ".")
                        check(text.strip())
                    if tn1 >= te1  and flag1 == True:
                        print("Time started: " + time.ctime(tn1) + ", timeout will halt after " + time.ctime(tn1 + t1) + ".")
                        check(text.strip())
                    
                elif text.strip() == pw_2:
                    timout()
                    timer(pw_2)
                    if tb2 == tn2 and flag2 == True:
                        print("Time started: " + time.ctime(tn2) + ", timeout will halt after " + time.ctime(tb2 + t2) + ".")
                        check(text.strip())
                    elif tn2 >= te2 and flag2 == True:
                        print("Time started: " + time.ctime(tn2) + ", timeout will halt after " + time.ctime(tn2 + t2) + ".")
                        check(text.strip())
                
finally:
        pwm.stop()
        GPIO.cleanup()
