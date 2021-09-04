from mqtt_client import MQTTClient 
import ubinascii
import config
import machine 
import time 
 
def sub_cb(topic, msg): 
   print(msg) 
 
MQTT_USERNAME = config.MQTT_USERNAME
MQTT_API = config.MQTT_API
MQTT_FEED = config.MQTT_FEED
CLIENT_ID = ubinascii.hexlify(machine.unique_id()) 

client = MQTTClient(CLIENT_ID, "io.adafruit.com",user=MQTT_USERNAME, password=MQTT_API, port=1883) 
client.set_callback(sub_cb) 
client.connect()
client.subscribe(topic=MQTT_USERNAME+"/Feeds/"+MQTT_FEED) 
print("Connected to the MQTT broker")

while True: 
    print("Sending ON") 
    # client.publish(topic=MQTT_USERNAME+"/feeds/"+MQTT_FEED, msg="1")
    # time.sleep(5) 
    # print("Sending OFF") 
    # client.publish(topic=MQTT_USERNAME+"/feeds/"+MQTT_FEED, msg="0")
    # time.sleep(5) 