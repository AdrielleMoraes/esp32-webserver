import time
from machine import Pin
import gc
try:
  import usocket as socket
except:
  import socket

# import firebase_admin
# from hcsr04 import HCSR04
# import homePage

import ufirebase

def StartDB():
    print('Connecting to firebase DB')
    fb = ufirebase.get('https://boilercontrol-iot-default-rtdb.europe-west1.firebasedatabase.app/esp32/Name.json')
    print(fb)

def led_control():  
    # set pins
    led = Pin(12, Pin.OUT)
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    # create web socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    # distance sensor data
    sensor = HCSR04(trigger_pin=27, echo_pin=26,echo_timeout_us=1000000)

    while True:

        # read data
        distance = sensor.distance_cm()

        try:
            if gc.mem_free() < 102000:
                gc.collect()
            conn, addr = s.accept()
            conn.settimeout(3.0)
            print('Received HTTP GET connection request from %s' % str(addr))
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            print('GET Rquest Content = %s' % request)
            led_on = request.find('/?on')
            led_off = request.find('/?off')

            if led_on == 6:
                print('LED ON -> GPIO2')
                led_state = "ON"
                led.value(1)

            if led_off == 6:
                print('LED OFF -> GPIO2')
                led_state = "OFF"
                led.value(0)


            response = homePage.web_page(data=str(distance))

            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()

        except OSError as e:
            conn.close()
            print('Connection closed')

def main(): 
    StartDB()