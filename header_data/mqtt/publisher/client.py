import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    print("Connectied with result code", rc)

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883, 60)
start_time = time.time()
headers = {'header' + str(i): "value" + str(i) for i in range(200000)} #6MB
payload = json.dumps({"headers": headers, "start_time": start_time})

client.publish("test/topic", payload)
client.disconnect()