from paho.mqtt import client as mqtt_client 
import random  
import time
import secrets
from struct import *
   
  
client_id = f'boiler-sensor-{random.randint(0, 1000)}'  

def connect_mqtt(MQTT_USERNAME, MQTT_API, MQTT_BROKER, MQTT_PORT):     
    def on_connect(client, userdata, flags, rc):
        if rc==0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)
            
    client = mqtt_client.Client(client_id)
    client.username_pw_set(MQTT_USERNAME, MQTT_API)     
    client.on_connect = on_connect     
    client.connect(MQTT_BROKER, MQTT_PORT)     
    return client   
    
        
def publish(client, feed_user, feed_id):
    msg = 1
    result = client.publish('{0}/feeds/{1}'.format(feed_user, feed_id), payload = msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{'{0}/feeds/{1}'.format(feed_user, feed_id)}`")
    else:
        print(f"Failed to send message to topic {'{0}/feeds/{1}'.format(feed_user, feed_id)}")
        
def subscribe(client: mqtt_client, feed_user, feed_id):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe('{0}/feeds/{1}'.format(feed_user, feed_id))
    client.on_message = on_message


def main():     
    MQTT_USERNAME = secrets.MQTT_USERNAME
    MQTT_API = secrets.MQTT_API
    MQTT_TOPIC_STATE = secrets.MQTT_TOPIC_STATE
    MQTT_TOPIC_TEMP = secrets.MQTT_TOPIC_TEMP
    MQTT_BROKER = secrets.MQTT_BROKER
    MQTT_PORT = secrets.MQTT_PORT

    client = connect_mqtt(MQTT_USERNAME, MQTT_API,MQTT_BROKER, MQTT_PORT)   
    # client.loop_start()
    publish(client, MQTT_USERNAME, MQTT_TOPIC_STATE) 
    # subscribe(client, MQTT_USERNAME,MQTT_TOPIC_TEMP)
    client.loop_forever()
     
 
    
if __name__ == '__main__':     
    main()