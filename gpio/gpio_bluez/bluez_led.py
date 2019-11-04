import RPi.GPIO as GPIO

from bluetooth import *

server = BluetoothSocket(RFCOMM)
server.bind(("", PORT_ANY))
server.listen(3)

client, info = server.accept()


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin1 = 14
led_pin2 = 15

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)


while True:
    data = client_sock.recv (1024)
    print("received [%s]" %data)
    if len (data) == 0:
        break
    elif (data == "1"):
        GPIO.output(led_pin1, GPIO.HIGH)
    elif (data == "0"):
        GPIO.output(led_pin1, GPIO.LOW)
