import RPi.GPIO as GPIO
from bluetooth import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin1 = 14
led_pin2 = 15


GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

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
            break
        elif (data == "1"):
            GPIO.output(led_pin1, GPIO.HIGH)
        elif (data == "0"):
            GPIO.output(led_pin1, GPIO.LOW)


except IOError:
    pass
finally:
    GPIO.cleanup()
    print("disconnected")
    client_sock.close()
    server_sock.close()
    print("all done")
