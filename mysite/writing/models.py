# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DOCUMENT_LINK_PERMISSION_CHOICES = (
    (0, 'can-view'),
    (1, 'can-comment'),
    (2, 'can-edit')
)


class Writer(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return r"%s"%self.user


class Document(models.Model):
    title = models.TextField(max_length=200, blank=True)
    writer = models.ForeignKey(Writer, related_name='documents', on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def get_username(self):
        return self.writer.user

    def __unicode__(self):
        return self.title


class DocumentLink(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    doc = models.ForeignKey(Document, null=False, related_name='shared', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Writer, related_name='document_link_to_user')
    permission = models.IntegerField(default=0, choices=DOCUMENT_LINK_PERMISSION_CHOICES)
    modified = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "Shared '%s' with '%s'"%(self.doc.title, self.to_user.user)
