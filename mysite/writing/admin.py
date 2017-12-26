# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Writer, Document

# Register your models here.

class WriterAdmin(admin.ModelAdmin):
    list_display = ('user',)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uuid', 'writer')


admin.site.register(Writer, WriterAdmin)
admin.site.register(Document, DocumentAdmin)
