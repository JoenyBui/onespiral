# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Writer(models.Model):
    user = models.OneToOneField(User)


class Document(models.Model):
    title = models.TextField(max_length=200, blank=True)
    user = models.ForeignKey(Writer)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    