# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Teacher, Student, Class, ClassroomPasscode


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',)
    readonly_fields = ('uuid',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)
    readonly_fields = ('uuid',)


class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    readonly_fields = ('uuid',)


class ClassroomPasscodeAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'passcode')
    readonly_fields = ('passcode',)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(ClassroomPasscode, ClassroomPasscodeAdmin)
