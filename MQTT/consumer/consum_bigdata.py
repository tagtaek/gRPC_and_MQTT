import paho.mqtt.client as mqtt
import time
import json

message_count = 0
threshold = 5
down_start_time = 0

def on_message(client, userdata, msg):
    # down_start_time 변수를 전역 변수로 선언했지만, on_message 함수 내부에서 이 변수를 
    # 수정하려고 하면, 파이썬은 이를 지역 변수로 인식합니다. 
    # 따라서 global 키워드를 사용하여 on_message 함수 내에서 전역 변수를 참조하게 해야 
    global message_count, down_start_time
    message_count += 1

    message = json.loads(msg.payload) # JSON 문자열을 Python 객체로 변환
    start_time = message['start_time']
    current_time = time.time()
    
    delay = current_time - start_time
    print(f"Message delay: {delay} seconds")
    
    if message_count == 1:
        down_start_time = time.time()

    if message_count == threshold:
        current_time = time.time()
        end_time = current_time - down_start_time
        print(f"Consuming takes {end_time} seconds")
        
broker = "localhost"
port = 1883
topic = "test/topic"

client = mqtt.Client()
client.on_connect = lambda client, userdata, flags, rc: client.subscribe(topic)
client.on_message = on_message

client.connect(broker, port, 60)

print('Waiting for messages. To exit press CTRL+C')
client.loop_forever()
