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
        fields = ('id', 'uuid', 'title', 'writer', 'created', 'modified')


class DocumentHyperlinkSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Document
        fields = ('url', 'uuid', 'title', 'writer')
        extra_kwargs = {
            'url': {
                'view_name': 'v1:writing:document-detail',
                'lookup_field': 'uuid'
            }

            # lookup_field='uuid'
        }