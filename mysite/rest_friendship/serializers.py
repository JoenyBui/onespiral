# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from friendship.models import Friend, FriendshipRequest, Follow
from .utils import import_from_string

config = apps.get_app_config('rest_friendship')


class UserField(serializers.Field):
    def to_representation(self, value):
        return value.profile.uuid

    def to_internal_value(self, data):
        return User.objects.get(profile__uuid=data)


class UserSerializer(serializers.ModelSerializer):
    uuid = serializers.ReadOnlyField(source='profile.uuid')
    full_name = serializers.SerializerMethodField(source='get_full_name')
    avatar = serializers.ReadOnlyField(source='profile.avatar')

    class Meta:
        model = User
        fields = ('uuid', 'full_name', 'first_name', 'last_name', 'email', 'avatar')

    def get_full_name(self, obj):
        return obj.get_full_name()


class FriendsSerializer(serializers.ModelSerializer):
    to_user = UserField()
    # to_user_uuid = serializers.ReadOnlyField(source='to_user.profile.uuid')
    to_user_name = serializers.ReadOnlyField(source='to_user.get_full_name')
    from_user = UserField()
    # from_user_uuid = serializers.ReadOnlyField(source='from_user.profile.uuid')
    from_user_name = serializers.ReadOnlyField(source='from_user.get_full_name')

    class Meta:
        model = Friend
        fields = ('to_user', 'to_user_name', 'from_user', 'from_user_name', 'created')


class FriendshipRequestSerializer(serializers.ModelSerializer):
    to_user = UserField()
    from_user = UserField()

    class Meta:
        model = FriendshipRequest
        fields = ('from_user', 'to_user', 'message', 'created', 'rejected', 'viewed')


class FollowSerializer(serializers.ModelSerializer):
    follower = UserField()
    followee = UserField()

    class Meta:
        model = Follow
        fields = ('follower', 'followee', 'created')


def get_user_serializer():
    return import_from_string(config.user_serializer, 'USER_SERIALIZER')
