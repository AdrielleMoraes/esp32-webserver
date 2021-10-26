from paho.mqtt import client as mqtt_client 
import random  
import time



client_id = f'python-mqtt-{random.randint(0, 1000)}' 

deviceId = "deviceId"   

def connect_mqtt():     
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
      
        
def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(MQTT_TOPIC_STATE, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{MQTT_TOPIC_STATE}`")
        else:
            print(f"Failed to send message to topic {MQTT_TOPIC_STATE}")
        msg_count += 1
        
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(MQTT_TOPIC_TEMP)
    client.on_message = on_message


def main():     
    client = connect_mqtt()     
    # client.loop_start()
    # publish(client)  
    subscribe(client)
    client.loop_forever()
     
 
    
if __name__ == '__main__':     
    main()

