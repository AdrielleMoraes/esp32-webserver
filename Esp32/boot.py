# This file will first run 
# import config 
# import run

# import network

# import gc
# gc.collect()

# # implement mqtt instead with autoconnect
# ssid = config.SSID
# password = config.WIFI_PASSWORD

# station = network.WLAN(network.STA_IF)

# station.active(True)
# station.connect(ssid, password)

# while station.isconnected() == False:
#   pass

# print('Connection successful')
# print(station.ifconfig())

import wifimgr # wifi manager to handle wifi connectivity
from time import sleep
import run

try:
  import usocket as socket
except:
  print("Importing socket instead")
  import socket

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D

# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")

print("Starting Server...")
run.main()


