import pika
import time
import sys

def connect_to_rabbitmq(host):
    retry_count = 0
    while retry_count < 5:
        try:
            return pika.BlockingConnection(pika.ConnectionParameters(host=host))
        except pika.exceptions.AMQPConnectionError:
            retry_count += 1
            print(f"Failed to connect to RabbitMQ. Retrying in 5 seconds... (Attempt {retry_count})")
            time.sleep(5)
    print("Failed to connect after 5 attempts.")
    sys.exit(1)

def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")

def start_consuming(channel):
    channel.basic_consume(queue='ABC', on_message_callback=callback, auto_ack=True)
    print('Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Consumer stopped by user.")
        channel.stop_consuming()

def main():
    host = input("Enter RabbitMQ host (default 'localhost'): ") or 'localhost'
    connection = connect_to_rabbitmq(host)
    channel = connection.channel()
    channel.queue_declare(queue='ABC')
    start_consuming(channel)
    channel.close()
    connection.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
