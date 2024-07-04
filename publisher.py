import pika
import sys
import time

def connect_to_rabbitmq():
    try:
        return pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    except pika.exceptions.AMQPConnectionError:
        print("Failed to connect to RabbitMQ. Is the service running?")
        sys.exit(1)

def send_messages(channel, num_messages):
    for i in range(num_messages):
        message = f"Message number {i}"
        channel.basic_publish(exchange='', routing_key='ABC', body=message)
        print(f"Sent: {message}")
        time.sleep(1)  # Simulate processing time

def main():
    connection = connect_to_rabbitmq()
    channel = connection.channel()
    channel.queue_declare(queue='ABC')
    
    try:
        num_messages = int(input("Enter the number of messages to send: "))
        send_messages(channel, num_messages)
    except ValueError:
        print("Please enter a valid integer for the number of messages.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        connection.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
