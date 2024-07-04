import pika
import time
import sys

def connect_to_rabbitmq():
    while True:
        try:
            return pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        except pika.exceptions.AMQPConnectionError:
            print("Failed to connect to RabbitMQ. Retrying in 5 seconds...")
            time.sleep(5)

def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")

def start_consuming(channel):
    channel.basic_consume(queue='ABC', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Consumer stopped by user.")

def main():
    connection = connect_to_rabbitmq()
    channel = connection.channel()
    channel.queue_declare(queue='ABC')
    start_consuming(channel)
    connection.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
