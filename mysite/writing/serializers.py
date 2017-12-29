from urlparse import urljoin

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.reverse import reverse

from drf_haystack.serializers import HaystackSerializer

from .models import Writer, Document
from .search_indexes import DocumentIndex

__author__ = 'jbui'


class WriterSerializers(serializers.ModelSerializer):
    user_uuid = serializers.ReadOnlyField(source='user.profile.uuid')

    class Meta:
        model = Writer
        fields = ('user_uuid',)


class DocumentSerializers(serializers.ModelSerializer):
    user_uuid = serializers.ReadOnlyField(source='writer.user.profile.uuid')
    uuid = serializers.ReadOnlyField()

    class Meta:
        model = Document
        fields = ('uuid', 'title', 'user_uuid', 'created', 'modified')


class DocumentSearchSerializer(HaystackSerializer):

    class Meta:
        index_classes = [DocumentIndex]
        fields = [
            'text', 'title', 'user', 'uuid', 'autocomplete'
        ]
        ignore_fields = ["text", "autocomplete"]
        field_aliases = {
            "q": "autocomplete"
        }