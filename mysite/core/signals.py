from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from core.models import Profile


@receiver(pre_save, sender=User)
def create_firebase_user(sender, **kwargs):
    #TODO: When a new user is created, the same user is created in firebase.
    pass

@receiver(post_save, sender=User)
def create_profile_root(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)