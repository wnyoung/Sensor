import RPi.GPIO as GPIO
import time
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 0
GPIO_ECHO = 1

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, 1)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)

    GPIO.output(GPIO_TRIGGER, 0)
    StartTime = time.time()
    StopTime = time.time()


    while GPIO.input(GPIO_ECHO) == 1:
        StartTime = time.time()
        
    while GPIO.input(GPIO_ECHO) == 0:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime


    distance = (TimeElapsed * 34300) / 2
    return distance


if __name__ == "__main__":
    
    try:
        while True:
            dist = distance()
            print("Measured Distance = %.1f cm" %dist)
            time.sleep(1)
    

    except KeyboardInterrupt:
        print("Measurement stopped by USER")
        GPIO.cleanup ()
