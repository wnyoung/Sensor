#파이의 GPIO채널을 제어하는 모듈
import RPi.GPIO as GPIO
import time

#step2) GPIO를 BCM으로 설정한다.
GPIO.setmode(GPIO.BCM)

led_pin1 = 14
led_pin2 = 15

#step2) 해당 핀을 출력으로 설정한다.
#GPIO.setup(led_pin1, GPIO.OUT)
#GPIO.setup(led_pin2, GPIO.OUT)

chan_list = [led_pin1, led_pin2]
GPIO.setup(chan_list, GPIO.OUT)

#예외처리구문
try:
    while True:
        #step3) 프로그램의 제어구문에서 LED의 ON/OFF동작
        GPIO.output(led_pin1, False)    
        GPIO.output(led_pin2, True)
        #1초쉰다.
        time.sleep(1)
        GPIO.output(led_pin1, True)
        GPIO.output(led_pin2, False)
        time.sleep(1)
        
finally:
    print("Cleaning up")
    GPIO.cleanup()
