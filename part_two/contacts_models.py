from mongoengine import (
    Document,
    StringField,
    BooleanField,
)


class Contacts(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField()
    method_messaging = StringField(choices=["SMS", "Email"])
    delivery = BooleanField(required=True, default=False)
