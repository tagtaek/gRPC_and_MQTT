import paho.mqtt.client as mqtt
import time
import json

broker = "localhost"
port = 1883
topic = "test/topic"

client = mqtt.Client()
client.connect(broker, port, 60)

large_array = [i for i in range(12500000)]
start_time = time.time()  # 시작 타임스탬프 기록
upload_time = 0

for i in range(1, 6):
    message = {
        'data': large_array,
        'start_time': start_time
    }
    client.publish(topic, json.dumps(message)) # 메세지를 json으로 변환
    upload_time = time.time() - start_time
    print(f'Sent message {i}, uploading ended at {upload_time}')

client.disconnect()

# server start => sudo rabbitmq-server start
# queue check => sudo rabbitmqctl list_queues
# server stop => rabbitmqctl stop OR ctrl+C

# 1. server run
# 2. consumer run(listening..)
# 3. producer run