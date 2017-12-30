from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters
from rest_framework import generics

from rest_framework_extensions.mixins import NestedViewSetMixin

from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackAutocompleteFilter

from .models import Writer, Document, DocumentLink
from .search_indexes import DocumentIndex

from .serializers import WriterSerializers, DocumentSerializers, DocumentSearchSerializer, DocumentLinkSerializer


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


class DocumentSearchViewSet(HaystackViewSet):
    index_models = [Document]
    serializer_class = DocumentSearchSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = [HaystackAutocompleteFilter]


class MeWriterModelViewSet(WriterModelViewSet):

    def get_queryset(self):
        return Writer.objects.filter(user=self.request.user)
