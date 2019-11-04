import smbus
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

gpio_pin = 13
led_pin1 = 14

GPIO.setup(gpio_pin, GPIO.OUT)
GPIO.setup(led_pin1, GPIO.OUT)
scale = [ 261, 294, 329, 349, 392, 440, 493, 523 ]
p1 = GPIO.PWM(gpio_pin, 100)
p2 = GPIO.PWM(14, 50)

p1.start(0)
p2.start(0) #초기 듀티 사이클 설정

bus = smbus.SMBus(1)
addr = 0x40
cmd_temp = 0xf3
cmd_humi = 0xf5
soft_reset = 0xfe
temp = 0.0
humi = 0.0
val = 0
data = [0, 0]

try:
    bus.write_byte(addr, soft_reset)
    time.sleep(0.05)
    while True:
        # temperature
        bus.write_byte(addr, cmd_temp)
        time.sleep(0.26)
        for i in range(0,2,1):
            data[i] = bus.read_byte(addr)
        val = data[0] << 8 | data[1]
        temp = -46.85+175.72/65536* val
        # humidity
        bus.write_byte(addr, cmd_humi)
        time.sleep(0.26)
        for i in range(0,2,1):
            data[i] = bus.read_byte(addr)
        val = data[0] << 8 | data[1]
        humi = -6.0+125.0/65536* val

        print("temp : %.2f, humi : %.2f" %(temp, humi))
        
        time.sleep(1)
        if temp > 30:
            p1.ChangeDutyCycle(40)
            p2.ChangeDutyCycle(90)
            p1.ChangeFrequency(scale[2])
            
            time.sleep(1)
            p1.ChangeFrequency(scale[6])
            p2.ChangeDutyCycle(0)
        else:
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)
        #makin blink !!
        
except KeyboardInterrupt:
    p1.stop() # stop the PWM output
    GPIO.cleanup()
    
