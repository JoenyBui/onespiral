"""
Core Test Base Setting

"""
import os

from django.contrib.auth.models import User
from django.test import TestCase

from firebase_admin import auth


class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='_JohnDoe', password='password123', email='john.doe.1@email.com')

    def tearDown(self):
        # Clean up the user
        if self.user.profile:
            auth.delete_user(str(self.user.profile.uuid))

    def test_profile_created(self):
        self.user.save()
        self.assertIsNotNone(self.user.profile)


class TestFirebaseAuth(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='_JohnDoe', password='password123', email='john.doe.2@email.com')
        self.user.save()
        self.test_uid = str(self.user.profile.uuid)

    def tearDown(self):
        if self.user.profile:
            auth.delete_user(str(self.user.profile.uuid))

    def test_firebase_login(self):
        self.assertIsNotNone(auth.get_user(uid=self.test_uid))

    def test_minting_new_token(self):
        custom_token = auth.create_custom_token(self.test_uid)

        self.assertIsNotNone(custom_token)
