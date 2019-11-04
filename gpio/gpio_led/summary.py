import RPi.GPIO as GPIO
import time

led_pins = [14,15]

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pins, GPIO.OUT)

GPIO.output(led_pins, 1)



p = GPIO.PWM(14,50)
p.start(0)


p.ChangeDutyCycle(30)
p.stop()


GPIO.cleanup()
