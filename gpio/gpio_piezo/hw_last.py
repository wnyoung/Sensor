import RPi.GPIO as GPIO
import time
from pynput import keyboard

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
gpio_pin = 13

GPIO.setup(gpio_pin, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)

p = GPIO.PWM(gpio_pin, 100)
p.start(0)

keys = {'a' : 261, "s" : 294, "d" : 329, "f" : 349, "g" : 392, "h" : 440, "i":493,"j":523, "k":587, "l":659}

def link(key):
    try:
        if (key.char in keys):
            sound(keys[key.char])
    finally:
        pass

def sound(freq):
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(50)

def on_press(key):
    try:
        link(key)
        GPIO.output(14, True)
        
    except AttributeError:
        pass

def on_release(key):
    time.sleep(0.01)
    p.ChangeDutyCycle(0)
    GPIO.output(14, 0)

    if key == keyboard.Key.esc:
        print("프로그램을 종료합니다.")
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()



