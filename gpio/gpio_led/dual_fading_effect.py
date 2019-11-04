import RPi.GPIO as GPIO
import time     #time모듈을 불러온다.

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#BCM에서 led는 각 14번, 15번 
led_pin1 = 14
led_pin2 = 15

#setup함수: 해당 핀을 IN or OUT 으로 사용하겠다.
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)


p1 = GPIO.PWM(14, 50)
p2 = GPIO.PWM(15, 50)
p1.start(0) #초기 듀티 사이클 설정
p2.start(0)
try:
    while 1:
        for dc in range(0,101,1):
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(100-dc)
            
            time.sleep(0.01)

        for dc in range(100,-1,-1):
            p1.ChangeDutyCycle(dc)
            p2.ChangeDutyCycle(100-dc)
            time.sleep(0.01)

except KeyboardInterrupt: #cntl+c
    p1.stop()
    p2.stop()
    GPIO.cleanup()
            
