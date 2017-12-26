# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from writing.models import Writer, Document

from core.tests import _BaseUserTest

# Create your tests here.


class TestDocument(TestCase, _BaseUserTest):
    def setUp(self):
        _BaseUserTest.setUp(self)

    def tearDown(self):
        _BaseUserTest.tearDown(self)

    def test_new_document(self):
        writer = self.user.writer
        doc = Document.objects.create(writer=writer, title='test')
        self.assertIsNotNone(doc)
