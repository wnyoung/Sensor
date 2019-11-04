import RPi.GPIO as GPIO
import time

motor_pins = [4, 25, 12]
motor_RP = 4
motor_RN = 25
motor_EN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pins, GPIO.OUT)

p = GPIO.PWM(4, 100)
p.start(0)

p.ChangeDutyCycle(10)

p.stop()

GPIO.cleanup()
