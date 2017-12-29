# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Writer(models.Model):
    user = models.OneToOneField(User)


class DocumentLink(models.Model):
    from_user = models.ForeignKey(Writer, related_name='document_link_from_user')
    to_user = models.ForeignKey(Writer, related_name='document_link_to_user')
    permission = models.IntegerField(default=0)
    modified = models.DateTimeField(default=timezone.now)


class Document(models.Model):
    title = models.TextField(max_length=200, blank=True)
    writer = models.ForeignKey(Writer)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def get_username(self):
        return self.writer.user.username