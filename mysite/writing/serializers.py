from urlparse import urljoin

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.reverse import reverse

from drf_haystack.serializers import HaystackSerializer

from core.models import Profile
from .models import Writer, Document, DocumentLink
from .search_indexes import DocumentIndex

__author__ = 'jbui'


class WriterField(serializers.Field):
    def to_representation(self, value):
        return value.user.profile.uuid

    def to_internal_value(self, data):
        return Writer.objects.get(user__profile__uuid=data)


class WriterSerializers(serializers.ModelSerializer):
    user_uuid = serializers.ReadOnlyField(source='user.profile.uuid')
    full_name = serializers.SerializerMethodField(source='get_full_name')
    documents = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='uuid'
    )

    class Meta:
        model = Writer
        fields = ('user_uuid', 'full_name', 'documents')

    def get_full_name(self, obj):
        return obj.user.get_full_name()


class MeWriterSerializer(WriterSerializers):
    user_uuid = serializers.ReadOnlyField(source='user.profile.uuid')
    full_name = serializers.SerializerMethodField(source='get_full_name')
    shared_documents = serializers.SerializerMethodField(source='get_full_name')
    documents = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='uuid'
    )

    class Meta:
        model = Writer
        fields = ('user_uuid', 'full_name', 'shared_documents', 'documents')

    def get_full_name(self, obj):
        return obj.user.get_full_name()

    def get_shared_documents(self, obj):
        value = []
        for item in list(DocumentLink.objects.filter(to_user=obj.id)):
            value.append(item.uuid)

        return value


class DocumentSerializers(serializers.ModelSerializer):
    writer = WriterField()
    shared = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='uuid'
    )
    shared_user_uuid = serializers.SerializerMethodField(source='get_shared_user_uuid')

    class Meta:
        model = Document
        fields = ('uuid', 'title', 'writer', 'created', 'modified', 'shared', 'shared_user_uuid')
        read_only_fields = ('uuid', 'modified',)

    def get_shared_user_uuid(self, obj):
        # return self.shared_user_uuid
        value = []
        for item in obj.shared.all():
            value.append(item.to_user.user.profile.uuid)
        return value


class SharedDocumentSerializers(serializers.ModelSerializer):
    doc_uuid = serializers.SlugRelatedField(source='doc', queryset=Document.objects.all(), slug_field='uuid')
    to_user = WriterField()
    meta = serializers.SerializerMethodField(source='get_meta')

    class Meta:
        model = DocumentLink
        fields = ('uuid', 'doc_uuid', 'to_user', 'permission', 'modified', 'meta')
        read_only_fields = ('uuid', 'modified',)

    def get_meta(self, obj):
        return {
            'title': obj.doc.title,
            'created': obj.doc.created,
            'modified': obj.doc.modified
        }


class DocumentLinkSerializer(serializers.ModelSerializer):
    doc_uuid = serializers.SlugRelatedField(source='doc', queryset=Document.objects.all(), slug_field='uuid')
    to_user = WriterField()

    class Meta:
        model = DocumentLink
        fields = ('uuid', 'doc_uuid', 'to_user', 'permission', 'modified')
        read_only_fields = ('uuid', 'modified',)


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