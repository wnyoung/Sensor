import threading
import RPi.GPIO as GPIO
import time

#p = GPIO.PWM(gpio_pin, 100)

def func(second):
	GPIO.setmode(GPIO.BCM)
	gpio_pin = 4
	GPIO.setup(gpio_pin, GPIO.OUT)
	p = GPIO.PWM(gpio_pin, 100)
	
	p.start(100)
	p.ChangeDutyCycle(90)
	print("물 줄 시간입니다!")
	p.ChangeFrequency(261)
	time.sleep(0.5)
	p.ChangeFrequency(350)
	time.sleep(0.5)
	p.stop()

	t1 = threading.Timer(second, func, [second]).start()
    t1.daemon = True
