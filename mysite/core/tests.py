"""
Core Test Base Setting

"""
import os

from django.contrib.auth.models import User
from django.test import TestCase

from firebase_admin import auth


class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.user.save()

    def tearDown(self):
        # Clean up the user
        if self.user.profile:
            auth.delete_user(self.user.profile.uuid)

    def test_profile_created(self):
        self.assertIsNotNone(self.user.profile)


class TestFirebaseAuth(TestCase):

    def setUp(self):
        self.test_uid = 'eb31ec5c-eb47-4964-90e1-679c4d848d89'

    def test_firebase_login(self):
        self.assertIsNotNone(auth.get_user(uid=self.test_uid))

    def test_minting_new_token(self):
        custom_token = auth.create_custom_token(self.test_uid)

        self.assertIsNotNone(custom_token)
