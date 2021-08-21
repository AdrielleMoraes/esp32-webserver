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

# connect to database
run.main()



