from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Teacher, Student, Class

from .serializers import TeacherSerializer, StudentSerializers, ClassSerializer


__author__ = 'jbui'


class TeacherModelViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Teacher Viewset**

    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class StudentModelViewSets(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    **Student Viewset**

    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class ClassModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

