# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import filters


from rest_framework.decorators import detail_route, list_route
from friendship.models import Friend, FriendshipRequest, Follow
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .serializers import get_user_serializer, UserSerializer, FriendshipRequestSerializer, FriendsSerializer, FollowSerializer


class FriendsModelViewSets(viewsets.ReadOnlyModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('first_name', 'last_name', 'email')
    lookup_field = 'profile__uuid'

    def get_queryset(self):
        friends = Friend.objects.friends(user=self.request.user)
        return User.objects.filter(pk__in=[x.pk for x in friends])


class FriendshipModelViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendsSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return Friend.objects.filter(Q(from_user=self.request.user) | Q(to_user=self.request.user))


class FriendshipRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return FriendshipRequest.objects.filter(to_user=self.request.user)


class FollowModelViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    def get_queryset(self):
        return Follow.objects.filter(followee=self.request.user)


class _FriendViewSet(viewsets.ViewSet):
    """
    ViewSet for Friend model
    """

    serializer_class = get_user_serializer()

    def list(self, request):
        friends = Friend.objects.friends(request.user)
        serializer = self.serializer_class(friends, many=True)
        return Response(serializer.data)

    @list_route()
    def requests(self, request):
        friend_requests = Friend.objects.unrejected_requests(user=request.user)
        return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

    @list_route()
    def sent_requests(self, request):
        friend_requests = Friend.objects.sent_requests(user=request.user)
        return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

    @list_route()
    def rejected_requests(self, request):
        friend_requests = Friend.objects.rejected_requests(user=request.user)
        return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

    def create(self, request):
        """
        Creates a friend request

        POST data:
        - user_id
        - message
        """

        friend_obj = Friend.objects.add_friend(
            request.user,                                                     # The sender
            get_object_or_404(get_user_model(), pk=request.data['user_id']),  # The recipient
            message=request.data['message']
        )

        return Response(
            FriendshipRequestSerializer(friend_obj).data,
            status.HTTP_201_CREATED
        )


class _FriendshipRequestViewSet(viewsets.ViewSet):
    """
    ViewSet for FriendshipRequest model
    """

    @detail_route(methods=['post'])
    def accept(self, request, pk=None):
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk)
        friendship_request.accept()
        return Response(
            FriendshipRequestSerializer(friendship_request).data,
            status.HTTP_201_CREATED
        )

    @detail_route(methods=['post'])
    def reject(self, request, pk=None):
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk)
        friendship_request.reject()
        return Response(
            FriendshipRequestSerializer(friendship_request).data,
            status.HTTP_201_CREATED
        )
