import wifimgr # wifi manager to handle wifi connectivity
import esp
try:
  import usocket as socket
except:
  print("Importing socket instead")
  import socket

esp.osdebug(None)
import gc
gc.collect()

# connect to wifi
wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D
print('Connected to the internet!')

# follow to the main.py script...

