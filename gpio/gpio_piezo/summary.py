import RPi.GPIO as GPIO
import time

piezo_pin = 13
scale = [261, 294, 329, 349, 392, 440, 493, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezo_pin, GPIO.OUT)


p = GPIO.PWM(piezo_pin, 100)
p.start(100)

p.ChangeFrequency(scale[i])

p.stop()


GPIO.cleanup()
