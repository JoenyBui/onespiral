# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Writer, Document, DocumentLink

# Register your models here.


class WriterAdmin(admin.ModelAdmin):
    list_display = ('user',)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uuid', 'writer')


class DocumentLinkAdmin(admin.ModelAdmin):
    list_display = ('doc', 'to_user', 'permission', 'modified')


admin.site.register(Writer, WriterAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentLink, DocumentLinkAdmin)
