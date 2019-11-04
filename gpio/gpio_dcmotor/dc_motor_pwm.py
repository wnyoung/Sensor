import RPi.GPIO as GPIO
import time    

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


led_pin1 = 14
led_pin2 = 15
dc_motor_P = 4
dc_motor_N = 25
dc_moto_EN = 12

GPIO.setup(dc_motor_P, GPIO.OUT)
GPIO.setup(dc_motor_N, GPIO.OUT)
GPIO.setup(dc_moto_EN, GPIO.OUT)

p = GPIO.PWM(dc_motor_N,100)
p.start(0)

try:
    while True:
        p.ChangeDutyCycle(10)
        GPIO.output(dc_motor_N, False)
        GPIO.output(dc_moto_EN, True)
        print("angle : 10")
        time.sleep(5)
        p.ChangeDutyCycle(35)
        GPIO.output(dc_motor_N, False)
        GPIO.output(dc_moto_EN, True)
        print("angle : 35")
        time.sleep(5)
        p.ChangeDutyCycle(80)
        GPIO.output(dc_motor_N, False)
        GPIO.output(dc_moto_EN, True)
        print("angle : 80")
        time.sleep(5)
        print ('stop')
        GPIO.output(dc_moto_EN, False)
        time.sleep(3)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
