import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin1 = 14
led_pin2 = 15

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

def Blink(numTimes,speed):
    for i in range(0,numTimes):
        print ("Iteration " + str(i+1))
        GPIO.output(14,True)
        time.sleep(speed)
        GPIO.output(14,False)
        time.sleep(speed)
        print("Done")

iterations = input("Enter total number of times to blink: ")
speed = input("Enter lingth of each blink(seconds): ")

Blink(int(iterations),float(speed))

