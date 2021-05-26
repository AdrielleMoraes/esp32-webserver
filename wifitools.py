""" This module contains a couple of helper functions that allow the ESP8266 to connect to a WiFi network and make GET requests. """

import urequests

#https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_basics.html
def connect(SSID,password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def getmac():
    import network
    import ubinascii
    return ubinascii.hexlify(network.WLAN().config('mac'),':').decode()

def flaskiot_post(API_key,mac_address,field, data):
    if not isinstance(data, str):
        data = str(data)
    if not isinstance(field, str):
        field = str(field)
    # https://freetemp.org/update/API_key=ASCIISTR/mac=6c:rf:7f:2b:0e:g8/field=1/data=72.3
    base_url = 'https://freetemp.org/update'
    api_key_url = '/API_key=' + API_key
    mac_url = '/mac=' + mac_address
    field_url = '/field=' + field
    data_url = '/data=' + str(data)
    url = base_url + api_key_url + mac_url + field_url + data_url
    print(url)
    response = urequests.get(url)
    print(response.text)