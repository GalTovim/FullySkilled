import enum

from mongoengine import *

Roles = ('Admin', 'Employer', 'Employee')


class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    role = StringField(required=True, choices=Roles)
    photo = ImageField()
    meta = {'collection': 'Users'}


class Job(EmbeddedDocument):
    title = StringField(required=True, unique=True)
    description = StringField()
    applicants = ListField(StringField())


class Business(Document):
    name = StringField(required=True, unique=True)
    address = StringField()
    owner = ReferenceField(User, required=True)
    jobs = EmbeddedDocumentListField(Job)
    meta = {'collection': 'Businesses'}




