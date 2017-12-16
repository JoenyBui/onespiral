from django.db.models.signals import pre_save, post_save
from django.core.signals import request_finished
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User

from core.models import Profile


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

#TODO: Need to auto create profile if a user is created/register.
@receiver(post_save, sender=User)
def create_profile_root(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)