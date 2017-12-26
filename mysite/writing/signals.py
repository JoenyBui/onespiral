from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from firebase_admin import db

from writing.models import Writer, Document
from core.models import Profile


@receiver(post_save, sender=User)
def create_writer(sender, instance=None, created=False, **kwargs):
    if created:
        # Create a new writing row for a new user.
        Writer.objects.get_or_create(user=instance)


@receiver(post_save, sender=Document)
def create_new_document(sender, instance=None, created=False, **kwargs):
    if created:
        document = instance
        writer = document.writer
        profile = Profile.objects.get(user=writer.user)

        # Create New Document
        root = db.reference()

        # Add a new document
        root.child('documents/%s'%(str(document.uuid))).set({
            'owner': str(profile.uuid),

            # Need to get the same format as javascript
            # 'timestamp': str(datetime.now())
        })
