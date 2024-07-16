import pika
import time
import json

message_count = 0
threshold = 10000
down_start_time = time.time()

# callback 함수는 RabbitMQ에서 메시지를 수신할 때 호출되는 함수. 
# RabbitMQ는 메시지를 큐에서 소비자(콘슈머)에게 전달할 때마다 이 콜백 함수를 실행하여 메시지를 처리
def callback(ch, method, properties, body):
    global message_count
    message_count += 1

    message = json.loads(body) # JSON 문자열을 Python 객체로 변환
    start_time = message['start_time']
    current_time = time.time()
    
    delay = current_time - start_time
    print(f"Message {message['data']} delay: {delay} seconds")
    
    if message_count == threshold:
        current_time = time.time()
        end_time = current_time - down_start_time
        print(f"All data consume at {end_time} seconds")
        

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test_queue')

channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
