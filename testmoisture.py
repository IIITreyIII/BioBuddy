### Just a script to test the moisture sesnors not needed for main.py


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
sen1 = 22  # Update this to your sensor pin
sen2 = 23
sen3 = 24
sen4 = 25
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

#GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # or GPIO.PUD_UP


try:
    while True:
        print(GPIO.input(sen1)) + str("sensor 1")
        print(GPIO.input(sen2)) + ("sensor 2")
        print(GPIO.input(sen3)) + ("sensor 3")
        print(GPIO.input(sen4)) + ("sensor 4")
        time.sleep(1)
finally:
    GPIO.cleanup()
