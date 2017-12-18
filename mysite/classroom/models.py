# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    user = models.OneToOneField(User, null=True)


class Student(models.Model):
    """
    **Student Model**

    :user:
        User Model

    :teachers:
        Sensei objects

    """
    user = models.OneToOneField(User)

    def __str__(self):
        return '%s %s'%(self.user.first_name, self.user.last_name)

    # def get_absolute_url(self):
    #     return reverse('student-detail', args=[str(self.id)])


class Class(models.Model):
    """
    Class Model

    """
    name = models.CharField(default='Classroom Name', max_length=100)
    teacher = models.ForeignKey(Teacher)
    students = models.ManyToManyField(Student)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    modified = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s' % self.name


class ClassroomPasscode(models.Model):
    """
    This is a passcode used to connect users to the room.

    """
    classroom = models.ForeignKey(Class)
