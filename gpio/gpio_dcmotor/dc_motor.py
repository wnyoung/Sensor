import RPi.GPIO as GPIO
import time    

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


led_pin1 = 14
led_pin2 = 15
dc_motor_P = 4
dc_motor_N = 25
dc_moto_EN = 12


GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

GPIO.setup(dc_motor_P, GPIO.OUT)
GPIO.setup(dc_motor_N, GPIO.OUT)
GPIO.setup(dc_moto_EN, GPIO.OUT)

try:
    while True:
        print ("forword")
        GPIO.output(dc_motor_P, True)
        GPIO.output(dc_motor_N, False)
        GPIO.output(dc_moto_EN, True)
        time.sleep(1)
        
        print ("stop")
        GPIO.output(dc_moto_EN, False)
        time.sleep(1)
        
        print ("backword")
        GPIO.output(dc_motor_P, False)
        GPIO.output(dc_motor_N, True)
        GPIO.output(dc_moto_EN, True)
        time.sleep(1)
        print ("stop")
        GPIO.output(dc_moto_EN, False)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

