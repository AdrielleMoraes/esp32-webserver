import network
import config

def connect():
    _ssid = config.SSID
    _passw = config.WIFI_PASSWORD
    print(_ssid)
    print(_passw)
    sta = network.WLAN(network.STA_IF)
    sta.active(True)

    sta.connect(_ssid,_passw)

    print(sta.isconnected())
    print(sta.ifconfig())