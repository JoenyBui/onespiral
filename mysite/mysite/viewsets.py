from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from rest_framework.generics import RetrieveUpdateAPIView

from rest_framework_extensions.mixins import NestedViewSetMixin

from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackAutocompleteFilter

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db.models import Q

from mysite.serializers import MeProfileSerializer, MeDocumentSerializers

from writing.viewsets import WriterModelViewSet
from writing.serializers import MeWriterSerializer, DocumentSerializers, DocumentLinkSerializer
from writing.models import Writer, Document, DocumentLink

from friendship.models import Friend, FriendshipRequest, Follow
from rest_friendship.serializers import get_user_serializer, UserSerializer, FriendshipRequestSerializer, FriendsSerializer, FollowSerializer


class MeProfileView(RetrieveUpdateAPIView):
    serializer_class = MeProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        return self.request.user


class MeWriterViewSet(WriterModelViewSet):
    serializer_class = MeWriterSerializer

    def get_queryset(self):
        return Writer.objects.filter(user=self.request.user)


class MeDocumentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = MeDocumentSerializers
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # lookup_field = 'uuid'

    # def get_queryset(self):
    #     return Document.objects.filter(writer=self.request.user.writer)
    def get_queryset(self):
        return Document.objects.filter(writer=self.request.user.writer.id)

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user.writer)


class MeDocumentLinkViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = DocumentLink.objects.all()
    serializer_class = DocumentLinkSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return DocumentLink.objects.filter(to_user=self.request.user.writer.id)


class MeSharedDocumentModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
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


class MeFriendModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        friends = Friend.objects.friends(user=self.request.user)
        return User.objects.filter(pk__in=[x.pk for x in friends])


class MeFriendshipToUserModelViewSets(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendsSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return Friend.objects.filter(to_user=self.request.user)


class MeFriendshipFromUserModelViewSets(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendsSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return Friend.objects.filter(from_user=self.request.user)


class MeFriendshipToUserRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return FriendshipRequest.objects.filter(to_user=self.request.user)


class MeFriendshipFromUserRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return FriendshipRequest.objects.filter(from_user=self.request.user)


class MeFollowFolloweeModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return Follow.objects.filter(followee=self.request.user)


class MeFollowFollowerModelViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)
