from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Writer, Document

from .serializers import WriterSerializers, DocumentSerializers


__author__ = 'jbui'


class WriterModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Writer.objects.all()
    serializer_class = WriterSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class DocumentModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

