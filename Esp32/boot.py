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

# connect to database
run.main()



