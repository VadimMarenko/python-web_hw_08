import time

import pika

import connect
from contacts_models import Contacts

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.queue_declare(queue="SMS", durable=True)
print(" [*] Waiting for messages. To exit press CTRL+C")


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contacts.objects(id=contact_id).first()
    if contact:
        print(f"The message was sent to the phone number: {contact.phone_number}")
        contact.delivery = True
        contact.save()


channel.basic_consume(queue="SMS", on_message_callback=callback)

channel.start_consuming()