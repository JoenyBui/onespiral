from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from firebase_admin import auth

from mysite.firebase import fb_app
from core.models import Profile


@receiver(post_save, sender=User)
def create_profile_root(sender, instance=None, created=False, **kwargs):
    if created:
        # Create a new profile row for the new user.
        Profile.objects.get_or_create(user=instance)


@receiver(post_save, sender=Profile)
def create_firebase_user(sender, instance=None, created=False, **kwargs):
    if created:
        profile = instance
        user = User.objects.get(profile=instance)

        # Create firebase user
        fb_user = auth.create_user(uid=str(profile.uuid),
                              display_name=user.username,
                              email=user.email,
                              email_verified=False,
                              app=fb_app)
