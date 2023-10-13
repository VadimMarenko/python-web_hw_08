import pika

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5671, credentials=credentials)
)
channel = continue.channel()

channel.queue_declare(queue="hello")

if __name__ == "__main__":
    
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!'.encode()))
    print(" [x] Sent 'Hello World!'")
    connection.close()