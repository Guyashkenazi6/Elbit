import pika
import sys
import time

def connect_to_rabbitmq(host):
    while True:
        try:
            return pika.BlockingConnection(pika.ConnectionParameters(host=host))
        except pika.exceptions.AMQPConnectionError:
            print("Failed to connect to RabbitMQ. Is the service running?")
            time.sleep(5)
        except KeyboardInterrupt:
            print("Publisher interrupted by user during connection attempt.")
            sys.exit(1)

def send_messages(channel, num_messages):
    try:
        for i in range(num_messages):
            message = f"Message number {i}"
            channel.basic_publish(exchange='', routing_key='ABC', body=message)
            print(f"Sent: {message}")
            time.sleep(1)  # Simulate processing time
    except KeyboardInterrupt:
        print("Publisher interrupted by user during message sending.")

def main():
    host = input("Enter RabbitMQ host (default 'localhost'): ") or 'localhost'
    connection = connect_to_rabbitmq(host)
    channel = connection.channel()
    channel.queue_declare(queue='ABC')
    
    try:
        num_messages = int(input("Enter the number of messages to send: "))
        send_messages(channel, num_messages)
    except ValueError:
        print("Please enter a valid integer for the number of messages.")
    finally:
        channel.close()
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
