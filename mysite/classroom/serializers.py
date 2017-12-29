from collections import OrderedDict

# from urllib.parse import urljoin
from urlparse import urljoin

from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Teacher, Student, Class, ClassroomPasscode


__author__ = 'jbui'


class TeacherSerializer(serializers.ModelSerializer):
    """
    Serialize Teacher Model

    """
    # links = serializers.SerializerMethodField(method_name='get_links_url', label='links')
    # info = serializers.SerializerMethodField(method_name='get_info_data', label='info')

    class Meta:
        model = Teacher
        fields = ('id', 'user')

    # def get_info_data(self, obj, *args, **kwargs):
    #     """
    #     Get the teacher information url.
    #
    #     :param obj:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     info = OrderedDict({})
    #
    #     try:
    #         info['user'] = str(obj.user)
    #     except User.DoesNotExist as e:
    #         info['user'] = str(e)
    #
    #     return info
    #
    # def get_links_url(self, obj, *args, **kwargs):
    #     user_url = urljoin(reverse('v1:editor:users-list', request=self.context['request']), str(obj.user.pk))
    #
    #     return dict(user=user_url)


class StudentSerializers(serializers.ModelSerializer):
    """
    Serialize Student Model

    """
    # links = serializers.SerializerMethodField(method_name='get_links_url', label='links')
    # info = serializers.SerializerMethodField(method_name='get_info_data', label='info')
    # uuid = serializers.ReadOnlyField(source='uuid')
    user_uuid = serializers.ReadOnlyField(source='user.profile.uuid')

    class Meta:
        model = Student
        fields = ('uuid', 'user_uuid', 'user')
        extra_kwargs = {'user': {'write_only': True}}

    # def get_info_data(self, obj, *args, **kwargs):
    #     """
    #     Get the pupil information url.
    #
    #     :param obj:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     info = OrderedDict({})
    #
    #     try:
    #         info['user'] = str(obj.user)
    #     except User.DoesNotExist as e:
    #         info['user'] = str(e)
    #
    #     return info

    # def get_links_url(self, obj, *args, **kwargs):
    #     user_url = urljoin(reverse('v1:editor:users-list', request=self.context['request']), str(obj.user.pk))
    #
    #     return dict(user=user_url)


class ClassSerializer(serializers.ModelSerializer):
    """
    Class Serializer

    """
    created = serializers.ReadOnlyField()
    modified = serializers.ReadOnlyField()

    class Meta:
        model = Class
        fields = ('id', 'created', 'modified', 'teacher', 'students', 'name')


class ClassroomPasscodeSerializer(serializers.ModelSerializer):
    classroom_uuid = serializers.ReadOnlyField(source='classroom.uuid')

    class Meta:
        model = ClassroomPasscode
        fields = ('classroom_uuid', 'classroom', 'passcode', )
        extra_kwargs = {'classroom': {'write_only': True}}