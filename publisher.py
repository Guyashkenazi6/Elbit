import pika
import time

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure the channel 'ABC' exists
channel.queue_declare(queue='ABC')

# Send 10 messages to the 'ABC' channel
for i in range(10):
    message = f'Message number {i}'
    channel.basic_publish(exchange='', routing_key='ABC', body=message)
    print(f"Sent: {message}")
    time.sleep(1)  # Optional delay to simulate real-world usage

# Close the connection
connection.close()
