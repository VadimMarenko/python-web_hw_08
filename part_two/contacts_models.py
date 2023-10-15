from mongoengine import (
    Document,
    StringField,
    BooleanField,
)


class Contacts(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField()
    delivery = BooleanField(required=True, default=False)
