from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import ProfileSerializer


class ProfileDetailViewSets(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

