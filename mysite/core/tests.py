"""
Core Test Base Setting

"""
import os

from django.contrib.auth.models import User
from django.test import TestCase


class TestProfile(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.user.save()

    def test_profile_created(self):
        self.assertIsNotNone(self.user.profile)
