import RPi.GPIO as GPIO
import time

led_pins = [14,15]

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pins, GPIO.OUT)

def blink():
    for i in range(0,11):
        GPIO.output(led_pins, 0)
        time.sleep(1)

        GPIO.output(led_pins, 1)
        time.sleep(0)

        print(i)

try:
    blink()
except KeyboardInterrupt:
    print("exit")
finally:
    print("finally")
    GPIO.cleanup()
