from AHT10 import readSensor
import time
from mqtt_client import MQTTRunner

# Frequency of readings
last_message = 0
message_interval = 300 # every 5min


# start mqtt server
client_mqtt = MQTTRunner()

client_mqtt.connect()


# read data from sensors

sensor = readSensor() # Initialise temperature sensor

while(True):
    if (time.time() - last_message) > message_interval:
        last_message = time.time()
        temp = sensor.readTemp()
        client_mqtt.publish(value = temp)


# send data from sensors to mqtt server