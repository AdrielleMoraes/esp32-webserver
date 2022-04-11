from AHT10 import readSensor
import time
from mqtt_client import MQTTRunner

# Frequency of readings
last_message = 0
message_interval = 300 # every 5min


# connect to mqtt server
client_mqtt = MQTTRunner()
client_mqtt.connect()


# start sensor
sensor = readSensor() # Initialise temperature sensor

# main loop
while(True):
    if (time.time() - last_message) > message_interval:
        last_message = time.time()


        # read data from sensors
        temp = sensor.readTemp()


        # send data from sensors to mqtt server
        client_mqtt.publish(value = temp)

# create another routine to subscribe to a topic
