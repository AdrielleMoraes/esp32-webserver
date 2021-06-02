# This file will first run 
import config 
import run

import network

import gc
gc.collect()

ssid = config.SSID
password = config.WIFI_PASSWORD

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())


print("Starting Server...")
run.main()


