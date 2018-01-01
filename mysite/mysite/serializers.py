from rest_framework import serializers

from django.contrib.auth.models import User

from writing.serializers import WriterField
from writing.models import Writer, Document, DocumentLink


class UserField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return User.objects.get(profile__uuid=data)


class MeProfileSerializer(serializers.ModelSerializer):
    uuid = UserField(source='profile.uuid', read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    birth_date = serializers.DateField(source='profile.birth_date', allow_null=True)
    avatar = serializers.CharField(source='profile.avatar', allow_blank=True)

    class Meta:
        model = User
        fields = ('uuid', 'first_name', 'last_name', 'email', 'birth_date', 'avatar')


class MeDocumentSerializers(serializers.ModelSerializer):
    writer = WriterField()
    # shared = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='uuid'
    # )
    # shared_user_uuid = serializers.SerializerMethodField(source='get_shared_user_uuid')

    class Meta:
        model = Document
        fields = ('uuid', 'title', 'writer', 'created', 'modified')
        # read_only_fields = ('uuid', 'modified',)

    def get_shared_user_uuid(self, obj):
        # return self.shared_user_uuid
        value = []
        for item in obj.shared.all():
            value.append(item.to_user.user.profile.uuid)
        return value
