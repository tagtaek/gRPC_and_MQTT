import pika #rabbitmq library import

# If we wanted to connect to a broker on a different machine we'd simply specify its name or IP address here 'localhost'.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

# The queue name needs to be specified in the routing_key parameter
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()

# server start => sudo rabbitmqctl list_queues
# server stop => rabbitmqctl stop

# 1. server run
# 2. consumer run(listening..)
# 3. producer run