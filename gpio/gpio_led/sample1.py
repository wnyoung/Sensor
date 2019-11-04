import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin1 = 14
led_pin2 = 15

GPIO.setup(led_pin1, GPIO.IN)
GPIO.setup(led_pin2, GPIO.IN)

status_led1 = GPIO.input(led_pin1)
status_led2 = GPIO.input(led_pin2)

print("led_pin1: ",status_led1)
print("led_pin2: ",status_led2)

