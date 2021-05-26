"""
connect to the WiFi network
read the temperature off of the MCP9808 temperature sensor
try to post the temperature to our flask IoT server
wait 1 minute
"""

import wifitools
import readI2C
import time
import config
import random

def main():
    ssid = config.SSID
    password = config.WIFI_PASSWORD
    api_key = config.API_KEY
    mac_address = config.MAC_ADDRESS
    field = '1'

    wifitools.connect(ssid,password)
    time.sleep(5)

    for i in range(60*8):
        data = random.randint(0, 100)#readI2C.readValue()
        try:
            wifitools.flaskiot_post(api_key,mac_address,field,data)
        except:
            pass
        time.sleep(60)