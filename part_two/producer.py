import faker
import pika
import connect
from contacts_models import Contacts

fake = faker.Faker("uk_UA")
number_of_contacts = 25

Contacts.objects().delete()

for _ in range(number_of_contacts):
    phone = fake.phone_number()
    method_messg = "SMS" if phone.startswith("+") else "Email"

    contact = Contacts(
        fullname=fake.name(),
        email=fake.email(),
        phone_number=phone,
        method_messaging=method_messg,
        delivery=False,
    )
    contact.save()

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()


for contact in Contacts.objects():
    if contact.method_messaging == "SMS":
        queue_name = "SMS"

    if contact.method_messaging == "Email":
        queue_name = "Email"

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(exchange="", routing_key=queue_name, body=str(contact.id))

print(" [x] Sent messages")
connection.close()
