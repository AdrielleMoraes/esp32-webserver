import ubinascii
import config
import machine 
import time 
from umqtt.robust import MQTTClient
 

MQTT_USERNAME = config.MQTT_USERNAME
MQTT_API = config.MQTT_API
MQTT_FEED = config.MQTT_FEED
MQTT_BROKER = config.MQTT_BROKER
CLIENT_ID = ubinascii.hexlify(machine.unique_id()) 
MQTT_TOPIC = config.MQTT_TOPIC

led_state = machine.Pin(2, machine.Pin.OUT)
led_connected = machine.Pin(13, machine.Pin.OUT)
led_connected.value(0)

def sub_cb(topic, msg): 
  print(msg) 
  if msg == b'0':
    led_state.value(0)
  if msg == b'1':
    led_state.value(1)

def reset_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  led_connected.value(0)
  time.sleep(5)
  machine.reset()

print("Trying to connect to mqtt broker.")
try:
  client = MQTTClient(CLIENT_ID, MQTT_BROKER,user=MQTT_USERNAME, password=MQTT_API, port=1883) 
  client.DEBUG = True
  client.set_callback(sub_cb) 

  if not client.connect(clean_session=False):
    print("New session being set up")
    client.subscribe(topic=MQTT_TOPIC) 

except:
  reset_and_reconnect()


led_connected.value(1)

while True: 
  # correct erroe 23
  client.check_msg()
  time.sleep(1)
