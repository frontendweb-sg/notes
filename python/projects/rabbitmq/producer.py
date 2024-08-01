import pika

connection_parameter = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameter)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

message = "Hello, This is my first message"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"sent mesage: {message}")

connection.close()
