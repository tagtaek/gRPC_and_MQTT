import paho.mqtt.client as mqtt
import time
import json

def on_message(client, userdata, msg):

    message = json.loads(msg.payload)
    start_time = message['start_time']
    current_time = time.time()

    delay = current_time - start_time
    print(f"Message delay: {delay} seconds")

broker = "localhost"
port = 1883
topic = "test/topic"

client = mqtt.Client()
client.on_connect = lambda cleint, userdata, flags, rc: client.subscribe(topic)
client.on_message = on_message

client.connect(broker, port, 60)

print('Waiting for messages. To exit press CTRL+C')
client.loop_forever()