import RPi.GPIO as GPIO
import time
from pynput import keyboard

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
gpio_pin = 13
GPIO.setup(gpio_pin, GPIO.OUT)

scales = [ 261, 294, 329, 349, 392, 440, 493, 523 ]
keys = ['a', 's', 'd', 'f', 'g', 'h']

p = GPIO.PWM(gpio_pin, 100)
p.start(100)

def link(key):
    try:
        for i in range(6):
            if key.char == keys[i]:
                print("%s 눌렸습니다" %keys[i])
                sound(i)
    finally:
        pass

def sound(scale):
    p.ChangeFrequency(scales[scale])
    #p.ChangeDutyCycle(0)
    print("%s 울림니다" %scales[scale])
    time.sleep(1)

if __name__ == "__main__":
    try:
        while True:
            for i in keys:
                if keyboard.is_pressed('a'):
                    key = 'a'
                
                    print("%s 눌렸습니다" %key)
                    link(key)
    except KeyboardInterrupt:
        print("KeyboardInterrupt발생: 프로그램을 종료합니다.")
    finally:
        p.stop(0)
        GPIO.cleanup()



    
