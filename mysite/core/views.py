from django.shortcuts import render
from django.views import generic

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from core.models import Profile

from firebase_admin import auth


@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication, TokenAuthentication, JSONWebTokenAuthentication))
@permission_classes((IsAuthenticated,))
def get_firebase_minted_token(request, format=None):
    if request.user.is_authenticated():
        # Mint new authentication token to access firebase module.
        profile = Profile.objects.get(user=request.user)

        # Return the minted key.
        return Response({
            'token': auth.create_custom_token(uid=str(profile.uuid)),
            'uuid': str(profile.uuid)
        }, status=status.HTTP_200_OK)

    else:
        return Response({
            'token': None,
            'uuid': None
        }, status=status.HTTP_401_UNAUTHORIZED)
