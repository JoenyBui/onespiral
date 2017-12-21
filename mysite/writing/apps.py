# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class WritingConfig(AppConfig):
    name = 'writing'

    def ready(self):
        # Need to include signals
        import core.signals
