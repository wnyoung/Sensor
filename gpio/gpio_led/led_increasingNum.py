import RPi.GPIO as GPIO
import time     #time모듈을 불러온다.

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#BCM에서 led는 각 14번, 15번 
led_pin1 = 14
led_pin2 = 15

GPIO.setup(led_pin1, GPIO.OUT)

def blink(Num):
    for i in range(Num+1):
        GPIO.output(14, GPIO.HIGH)
        time.sleep(i*0.1)
        GPIO.output(14, GPIO.LOW)
        time.sleep(1)

In = int(input("Give times you want:"))
blink(In)
print("Program is terminated...")
GPIO.cleanup()
