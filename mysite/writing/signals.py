from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from writing.models import Writer


@receiver(post_save, sender=User)
def create_writer(sender, instance=None, created=False, **kwargs):
    if created:
        # Create a new writing row for a new user.
        Writer.objects.get_or_create(user=instance)

