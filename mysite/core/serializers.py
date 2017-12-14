from rest_framework import serializers

from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile Serializer

    """

    bio = serializers.CharField(source='profile.bio', allow_blank=True)
    location = serializers.CharField(source='profile.location', allow_blank=True)
    birth_date = serializers.DateField(source='profile.birth_date', allow_null=True)
    website = serializers.CharField(source='profile.website', allow_blank=True)
    twitter = serializers.CharField(source='profile.twitter', allow_blank=True)
    avatar = serializers.CharField(source='profile.avatar', allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'location', 'birth_date', 'website', 'twitter', 'avatar')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = super(ProfileSerializer, self).create(validated_data)
        self.create_or_update_profile(user, profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        self.create_or_update_profile(instance, profile_data)
        return super(ProfileSerializer, self).update(instance, validated_data)

    def create_or_update_profile(self, user, profile_data):
        profile, created = Profile.objects.get_or_create(user=user, defaults=profile_data)
        if not created and profile_data is not None:
            super(ProfileSerializer, self).update(profile, profile_data)

