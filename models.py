from mongoengine import (
    connect,
    Document,
    StringField,
    ReferenceField,
    CASCADE,
    ListField,
)


class Authors(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=30)
    born_location = StringField(max_length=50)
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField(max_length=150)
