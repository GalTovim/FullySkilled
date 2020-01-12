import enum

from mongoengine import *

Roles = ('Admin', 'Employer', 'Employee')


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(required=True, choices=Roles)
    city = StringField()
    street = StringField()
    apartment = IntField()
    email = StringField()
    phone = StringField()
    firstname = StringField()
    lastname = StringField()
    idnum = StringField()

    # Employee fields
    cv = FileField()

    photo = ImageField()
    meta = {'collection': 'Users'}


class Job(EmbeddedDocument):
    title = StringField(required=True)
    description = StringField()
    applicants = ListField(StringField())
    priority = BooleanField()
    address = StringField()
    business = StringField()


class Business(Document):
    name = StringField(required=True, unique=True)
    city = StringField()
    street = StringField()
    apartment = IntField()
    owner = ReferenceField(User, required=True)
    jobs = EmbeddedDocumentListField(Job)
    meta = {'collection': 'Businesses'}


class Faq(Document):
    question = StringField(required=True, unique=True)
    answer = StringField(required=True)
    number = IntField()
    meta = {'collection': 'FAQ'}
