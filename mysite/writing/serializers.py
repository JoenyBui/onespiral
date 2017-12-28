from urlparse import urljoin

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.reverse import reverse

from drf_haystack.serializers import HaystackSerializer

from .models import Writer, Document
from .search_indexes import DocumentIndex

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


class DocumentSearchSerializer(HaystackSerializer):

    class Meta:
        index_classes = [DocumentIndex]
        fields = [
            'text', 'title', 'user'
        ]