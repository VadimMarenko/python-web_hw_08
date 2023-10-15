import pika

import connect
from contacts_models import Contacts


def sent_message(email):
    print(f"The message sending to email: {email}")


def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contacts.objects(id=contact_id).first()
    if contact:
        sent_message(contact.email)
        contact.delivery = True
        contact.save()


credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()
channel.queue_declare(queue="Email", durable=True)
channel.basic_consume(queue="Email", on_message_callback=callback)
print(" [*] Waiting for messages. To exit press CTRL+C")

if __name__ == "__main__":
    channel.start_consuming()
