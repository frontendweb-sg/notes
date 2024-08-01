import pika
import sys
import os


def callback(ch, method, properties, body):
    print(f" [x] Received {str(body)}")


def main():
    # connection
    connection_parameter = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameter)

    # create a channel
    channel = connection.channel()

    # declare queue
    channel.queue_declare(queue='letterbox')

    channel.basic_consume(queue='letterbox', auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
