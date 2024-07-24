import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    start_time = data['start_time']
    current_time = time.time()
    delay = current_time - start_time

    print(f"Message delay: {delay} seconds")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()