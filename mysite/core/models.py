import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=30, blank=True)
    twitter = models.CharField(max_length=30, blank=True)
    avatar = models.CharField(max_length=30, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)


# Add additional methods to user
def get_uuid(**kwargs):
    pass


User.add_to_class('get_uuid', get_uuid)
