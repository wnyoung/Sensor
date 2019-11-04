import RPi.GPIO as GPIO
import time
from pynput import keyboard

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
gpio_pin = 13
GPIO.setup(gpio_pin, GPIO.OUT)

p = GPIO.PWM(gpio_pin, 100)
p.start(0)

scales = [ 261, 294, 329, 349, 392, 440, 493, 523, 587, 659 ]
keys = ['a', 's', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

def link(key):
    try:
        #print("%s"%key)
        for i in range(len(keys)):
            #print("%s 인가?" %keys[i])
            if key.char == keys[i]: #key == keys[i]라고 하면 안먹음
                #print("%s 눌렸습니다" %keys[i])
                sound(i)
                break
    finally:
        pass

def sound(scale):
    p.ChangeDutyCycle(50)
    p.ChangeFrequency(scales[scale])
    #p.ChangeDutyCycle(0)
    #print("%s 울림니다" %scales[scale])

def on_press(key):
    try:
        #print('alphanumeric key {0} pressed'.format(key.char))
        link(key)
    except AttributeError:
        pass

def on_release(key):
    time.sleep(0.01)
    p.ChangeDutyCycle(0)
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
