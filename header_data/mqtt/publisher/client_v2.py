import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    print("Connectied with result code", rc)

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883, 60)
start_time = time.time()
# 복잡한 헤더 구조
headers = {
    'header' + str(i): {
        "values": ["value" + str(i), "additional" + str(i)],
        "timestamp": time.time(),
        "details": {
            "sub_key1": "sub_value1_" + str(i),
            "sub_key2": "sub_value2_" + str(i)
        }
    } for i in range(50000)  # 6MB 이상의 큰 헤더 데이터
}
payload = json.dumps({"headers": headers, "start_time": start_time})

client.publish("test/topic", payload)
client.disconnect()