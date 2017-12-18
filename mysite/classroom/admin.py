# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Teacher, Student, Class


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
