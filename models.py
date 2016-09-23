# coding: utf-8

from mongoengine import *


class Task(Document):
    tid = StringField(required=True)
    # info = DictField(req)

