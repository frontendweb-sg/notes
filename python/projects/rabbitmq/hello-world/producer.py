import pika

# connection
connection_parameter = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameter)

# create a channel
channel = connection.channel()

# declare queue
channel.queue_declare(queue='letterbox')

# a message that will publish to the consumer
message = "Hello RabbigMQ, this is my first message"

# publish message
channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"messge sent: {message}")

# close the channel
channel.close()
