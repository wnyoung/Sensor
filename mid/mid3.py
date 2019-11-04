import RPi.GPIO as GPIO
from bluetooth import *
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

dc_motor_P = 4
dc_motor_N = 25
dc_moto_EN = 12

GPIO.setup(dc_motor_P, GPIO.OUT)
GPIO.setup(dc_motor_N, GPIO.OUT)
GPIO.setup(dc_moto_EN, GPIO.OUT)

p = GPIO.PWM(dc_motor_N,100)
p.start(0)

led_pin1 = 14
led_pin2 = 15


GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)


p1 = GPIO.PWM(14, 50)
p2 = GPIO.PWM(15, 50)
p1.start(0)

p2.start(0)

GPIO_TRIGGER = 0
GPIO_ECHO = 1

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN, pull_up_down = GPIO.PUD_UP)

gpio_pin = 13
GPIO.setup(gpio_pin, GPIO.OUT)
p3 = GPIO.PWM(gpio_pin, 100)
p3.start(0)

def distance():
    
    GPIO.output(GPIO_TRIGGER, 1)
    
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

server_sock = BluetoothSocket (RFCOMM)
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname ()[1]
uuid = "00000000-0000-1000-8000-00805F9B34FB"
advertise_service( server_sock , "raspberrypi",
                    service_id = uuid,
                    service_classes = [ uuid , SERIAL_PORT_CLASS],
                    profiles = [ SERIAL_PORT_PROFILE ], 
                )

print("Waiting for connection on RFCOMM channel %d" % port)
client_sock, client_info = server_sock.accept()
print("Accepted connection from ",client_info)
try:
    while True:
        data = client_sock.recv (1024)
        print("received [%s]" %data)
        if data =="quit":
            msg ="APP is terminated!!"            
            print(msg)
            client_sock.send(msg.encode())
      
            break
        elif (data == "1"):
            msg = "DC motor is working!!"
            print(msg)
            client_sock.send(msg.encode())
                
            p.ChangeDutyCycle(50)
            GPIO.output(dc_motor_N, False)
            GPIO.output(dc_moto_EN, True)

            time.sleep(4)
            GPIO.output(dc_moto_EN, 0)
            time.sleep(1)
            GPIO.output(dc_motor_N, True)
            GPIO.output(dc_moto_EN, True)
            time.sleep(4)
            GPIO.output(dc_moto_EN, 0)
            

        elif (data == "2"):
            msg = "LED fading effect!!"

            print(msg)
            client_sock.send(msg.encode())
            p1.ChangeDutyCycle(90)
            p2.ChangeDutyCycle(90)

            for dc in range(0,101,1):
                p1.ChangeDutyCycle(dc)
                p2.ChangeDutyCycle(100-dc)
                    
                time.sleep(0.01)

            for dc in range(100,-1,-1):
                p1.ChangeDutyCycle(dc)
                p2.ChangeDutyCycle(100-dc)
                time.sleep(0.01)
        elif (data == "3"):
            msg = "now in safe!"

            print(msg)
            client_sock.send(msg.encode())
  
            while True:
                dist = distance()
                print(dist)
                time.sleep(0.3)
                
                if dist < 5:
                    break
                
            msg = "Intruders!"

            print(msg)
            client_sock.send(msg.encode())
            
            p3.ChangeDutyCycle(40)

            time.sleep(5)
            p3.ChangeDutyCycle(0)


except IOError:
    pass
finally:
    GPIO.cleanup()
    print("disconnected")
    client_sock.close()
    server_sock.close()
    print("all done")
