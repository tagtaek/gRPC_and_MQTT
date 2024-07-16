import pika
import time
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test_queue')

start_time = time.time()  # 시작 타임스탬프 기록
upload_time = 0

for i in range(1, 10001):
    message = {
        'data': i,
        'start_time': start_time
    }
    channel.basic_publish(exchange='',
                          routing_key='test_queue',
                          body=json.dumps(message)) # (python)메시지를 JSON 문자열로 변환하여 전송
    upload_time = time.time() - start_time
    print(f'Sent message {i}, upload end at {upload_time}')

connection.close()

# server start => sudo rabbitmq-server start
# queue check => sudo rabbitmqctl list_queues
# server stop => rabbitmqctl stop OR ctrl+C

# 1. server run
# 2. consumer run(listening..)
# 3. producer run