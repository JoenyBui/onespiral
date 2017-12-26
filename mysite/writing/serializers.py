from urlparse import urljoin

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Writer, Document

__author__ = 'jbui'


class WriterSerializers(serializers.ModelSerializer):

    class Meta:
        model = Writer
        fields = ('id', 'user')


class DocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'writer', 'uuid')