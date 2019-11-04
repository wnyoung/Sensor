import RPi.GPIO as GPIO
import time
import keyboard

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin1 = 14
led_pin2 = 15

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

p = GPIO.PWM(14, 50)
p.start(0) #초기 듀티 사이클 설정
try:
    while 1:
        
        for dc in range(0,101,1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)

        for dc in range(100,-1,-1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)

except KeyboardInterrupt: #cntl+c
    p.stop()
    GPIO.cleanup()
            
