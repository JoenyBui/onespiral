# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    """
    **Teacher Model**.

    :user:
        User Model

    :pen_name:
        Pen Name

    """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return self.user.get_full_name()


class Student(models.Model):
    """
    **Student Model**

    :user:
        User Model

    :teachers:
        Sensei objects

    """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.get_full_name()

    # def get_absolute_url(self):
    #     return reverse('student-detail', args=[str(self.id)])


class Class(models.Model):
    """
    Class Model

    """
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(default='Classroom Name', max_length=100)
    teacher = models.ForeignKey(Teacher)
    students = models.ManyToManyField(Student, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s' % self.name


def generate_passcode(length=10):
    return str(uuid.uuid4())[:length]


class ClassroomPasscode(models.Model):
    """
    This is a passcode used to connect users to the room.

    """
    classroom = models.ForeignKey(Class)
    passcode = models.CharField(max_length=10, default=generate_passcode, unique=True)

    def __str__(self):
        return "(%s, %s)"%(self.classroom.name, self.passcode)
