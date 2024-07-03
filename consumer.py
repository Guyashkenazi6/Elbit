import pika

def callback(ch, method, properties, body):
    print(f"Received: {body}")

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure the channel 'ABC' exists
channel.queue_declare(queue='ABC')

# Subscribe to the 'ABC' channel
channel.basic_consume(queue='ABC', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
