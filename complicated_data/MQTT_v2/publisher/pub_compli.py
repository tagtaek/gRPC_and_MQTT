import json
import paho.mqtt.client as mqtt
import time

# 시작 시간 측정
start_time = time.time()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

def run():
    # MQTT 클라이언트 설정
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish

    # MQTT 브로커에 연결
    client.connect("localhost", 1883, 60)

    # 큰 데이터 생성
    message = {
        "text": "A" * 50 * 1024 * 1024,  # 50MB text data
        "number": 123456,
        "float_number": 12345.6789,
        "flag": True,
        "string_list": ["string_{}".format(i) for i in range(2500000)],  # 대략 33MB
        "string_map": {"key_{}".format(i): "value_{}".format(i) for i in range(2000000)},  # 대략 43.8MB
        "nested": {"nested_text": "Nested Text", "nested_number": 789},
        'start_time': start_time
    }

    # JSON 형식으로 직렬화
    payload = json.dumps(message)

    # 데이터 전송
    client.publish("test/topic", payload, qos=0)

    # 연결 종료
    client.disconnect()

    # 전송 시간 출력
    end_time = time.time()
    print(f"Data sent in {end_time - start_time} seconds")

if __name__ == '__main__':
    run()
