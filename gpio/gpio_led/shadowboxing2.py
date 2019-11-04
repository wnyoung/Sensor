import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pins = [14,15]

GPIO.setup(14, GPIO.OUT)


p = GPIO.PWM(14, 50)
p.start(0)

try:
    while True:
        for dc in range(0,101,10):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)

        time.sleep(3)
        
        for dc in range(100, -1,-10):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)

        time.sleep(3)
except KeyboardInterrupt:
    print("keyinterr")
finally:
    p.stop()
    GPIO.cleanup()
