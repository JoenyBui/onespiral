from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from rest_framework import generics

from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework_extensions.mixins import NestedViewSetMixin

from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackAutocompleteFilter

from .models import Writer, Document, DocumentLink
from .search_indexes import DocumentIndex

from .serializers import WriterSerializers, DocumentSerializers, DocumentSearchSerializer, DocumentLinkSerializer, \
    SharedDocumentSerializers, MeWriterSerializer


__author__ = 'jbui'


class WriterModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):

    queryset = Writer.objects.all()
    serializer_class = WriterSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    lookup_field = 'user__profile__uuid'


class DocumentModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    lookup_field = 'uuid'

    # def get_queryset(self):
    #     return Document.objects.filter(writer=self.request.user.writer)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user.writer)


class DocumentLinkModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = DocumentLink.objects.all()
    serializer_class = DocumentLinkSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)


class SharedDocumentModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    lookup_field = 'uuid'

    def get_query_link(self):
        value = []
        for item in DocumentLink.objects.filter(to_user=self.request.user.writer.id):
            value.append(item.doc.pk)
        return value

    def get_queryset(self):

        return Document.objects.filter(pk__in=self.get_query_link())

    # def perform_create(self, serializer):
    #     serializer.save(writer=self.request.user.writer)


class SharedDocumentLinkViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = DocumentLink.objects.all()
    serializer_class = SharedDocumentSerializers
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    lookup_field = 'to_user__user__profile__uuid'


class DocumentSearchViewSet(HaystackViewSet):
    index_models = [Document]
    serializer_class = DocumentSearchSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = [HaystackAutocompleteFilter]


# class MeWriterModelViewSet(WriterModelViewSet):
#     serializer_class = MeWriterSerializer
#
#     def get_queryset(self):
#         return Writer.objects.filter(user=self.request.user)
