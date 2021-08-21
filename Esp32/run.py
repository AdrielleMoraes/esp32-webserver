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

def main(): 
    StartDB()