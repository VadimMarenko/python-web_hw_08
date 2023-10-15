import faker
import pika
import connect
from contacts_models import Contacts

fake = faker.Faker()
number_of_contacts = 25

Contacts.objects().delete()

for _ in range(number_of_contacts):
    contact = Contacts(
        fullname=fake.name(),
        email=fake.email(),
        phone_number=fake.phone_number(),
        delivery=False,
    )
    contact.save()

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5671, credentials=credentials)
)
channel = connection.channel()

channel.queue_declare(queue="hello")

if __name__ == "__main__":
    channel.basic_publish(
        exchange="", routing_key="hello", body="Hello World!".encode()
    )
    print(" [x] Sent 'Hello World!'")
    connection.close()
