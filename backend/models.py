import enum

from mongoengine import *

Roles = ('Admin', 'Employer', 'Employee')


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(required=True, choices=Roles)
    email = StringField(required=True)
    phone = StringField(required=True)
    id = StringField(required=True)
    firstname = StringField(required=True)
    lastname = StringField(required=True)

    # Employee fields
    cv = FileField()

    photo = ImageField()
    meta = {'collection': 'Users'}


class Job(EmbeddedDocument):
    title = StringField(required=True, unique=True)
    description = StringField()
    applicants = ListField(StringField())
    priority = BooleanField()


class Business(Document):
    name = StringField(required=True, unique=True)
    address = StringField()
    city = StringField()
    owner = ReferenceField(User, required=True)
    jobs = EmbeddedDocumentListField(Job)
    meta = {'collection': 'Businesses'}


class Faq(Document):
    question = StringField(required=True, unique=True)
    answer = StringField(required=True)
    number = IntField()
    meta = {'collection': 'FAQ'}

