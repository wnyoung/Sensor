import RPi.GPIO as GPIO
import time

jog_pins= [ 5, 6, 16, 20, 21]
led_pins = [14,15]
stat = [ 0, 0, 0, 0, 0]


GPIO.setmode(GPIO.BCM)
GPIO.setup(jog_pins, GPIO.IN)
GPIO.setup(led_pins, GPIO.OUT)


def blink(i):
    if i == 0:
        GPIO.output(led_pins[0], 1)
        time.sleep(1)
        GPIO.output(led_pins[0], 0)
    elif i ==1:
        GPIO.output(led_pins[1], 1)
        time.sleep(1)
        GPIO.output(led_pins[1], 0)
    elif i ==2:
        for j in range(5):
            GPIO.output(led_pins[1], 1)
            time.sleep(0.1)
            GPIO.output(led_pins[1], 0)
            time.sleep(0.1)
    elif i ==3:
        for j in range(5):
            p = GPIO.PWM(led_pins[1],100)
            p.start(0)

            p.ChangeDutyCycle(j*20)
            
            time.sleep(0.5)
        p.stop(0)


try:
    for i in range(5):
        cur_stat= 0

    while True:
        for i in range(5):
            cur_stat= GPIO.input(jog_pins[i])
            if cur_stat != stat[i]:
                stat[i] = cur_stat
                blink(i)
                
finally:
    print("Cleaning up")
    GPIO.cleanup()
