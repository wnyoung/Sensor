import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

gpio_pin = 13

GPIO.setup(gpio_pin, GPIO.OUT)

scale = [ 261, 294, 329, 349, 392, 440, 493, 523 ]
p = GPIO.PWM(gpio_pin, 100)

#GPIO.output(gpio_pin, True)
p.start(100) 
try:
    while True:
        print('hello')
        p.ChangeFrequency(scale[4])
        time.sleep(0.5)
        p.ChangeFrequency(scale[4])
        time.sleep(0.5)
        p.ChangeFrequency(scale[5])
        time.sleep(0.5)
        p.ChangeFrequency(scale[5])
        time.sleep(0.5)
        p.ChangeFrequency(scale[4])
        time.sleep(0.5)
        p.ChangeFrequency(scale[4])
        time.sleep(0.5)
        p.ChangeFrequency(scale[2])
        time.sleep(0.2)
except KeyboardInterrupt:
    p.stop() # stop the PWM output
    GPIO.cleanup()
