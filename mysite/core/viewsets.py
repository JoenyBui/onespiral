from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.generics import RetrieveUpdateAPIView

from drf_haystack.viewsets import HaystackViewSet
from drf_haystack.filters import HaystackAutocompleteFilter

from django.contrib.auth.models import User
from .serializers import ProfileSerializer, ProfileSearchSerializer


class ProfileDetailViewSets(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ProfileSearchViewSet(HaystackViewSet):
    index_models = [User]
    serializer_class = ProfileSearchSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = [HaystackAutocompleteFilter]
