import smbus2
import time
import RPi.GPIO as GPIO
import time

#setupLED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin1 = 14
led_pin2 = 15

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
p1 = GPIO.PWM(led_pin1, 50)
p2 = GPIO.PWM(led_pin1, 50)
p1.start(0)
p2.start(0)


#setupLIGHT
bus = smbus2.SMBus(1)
addr = 0x23
reset = 0x07
con_hr_mode = 0x10
data1 = 0
data2 = 0
val = 0
light_val = 0

try:
    bus.write_byte(addr, reset)
    time.sleep(0.05)
    while True:
        bus.write_byte(addr, con_hr_mode)
        time.sleep(0.2)
        data1 = bus.read_byte(addr)
        data2 = bus.read_byte(addr)
        val = (data1 << 8) | data2
        light_val = val / 1.2
        print("light_val = %.2f" %light_val)
        

        if (light_val<200):
            p1.ChangeDutyCycle(90)
            p2.ChangeDutyCycle(90)
        elif (200<light_val<400):
            p1.ChangeDutyCycle(50)
            p2.ChangeDutyCycle(50)
        elif (light_val>400):
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
        time.sleep(0.01)
        
except KeyboardInterrupt:
    # do not anything
    pass
finally:
    p.stop()
    GPIO.cleanup()
