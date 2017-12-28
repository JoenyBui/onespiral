# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from django.apps import apps
from django.contrib.auth import get_user_model
from rest_framework import serializers
from friendship.models import Friend, FriendshipRequest, Follow
from .utils import import_from_string

config = apps.get_app_config('rest_friendship')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email')


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('id', 'to_user', 'from_user', 'created')


class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ('id', 'from_user', 'to_user', 'message', 'created', 'rejected', 'viewed')


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('id', 'follower', 'followee', 'created')


def get_user_serializer():
    return import_from_string(config.user_serializer, 'USER_SERIALIZER')
