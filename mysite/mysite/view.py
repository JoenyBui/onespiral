import os

from django.shortcuts import render
from django.views.generic import View

from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.schemas import SchemaGenerator
from rest_framework import permissions

from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        stats = {
            'maths_count': None,
            'fractions_count': None,
            'additions_count': None,
            'subtractions_count': None,
            'multiplications_count': None,
            'divisions_count': None
        }

        return render(request, self.template_name, {
            'stats': stats
        })


@api_view(('GET', ))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    # return Response({
    #     "v1": reverse("v1-root", request=request, format=format),
    #     # "core": reverse("core ", request=request, format=format),
    #     "api token auth": reverse("api-token", request=request, format=format),
    #     # "documents": reverse("docs", request=request, format=format),
    #     # "accounts": reverse("rest-auth-root", request=request, format=format),
    #     # "docs": reverse("api_docs", request=request, format=format)
    # })
    return Response({
        "v1": reverse("v1-root", request=request, format=format),
        "friendship": reverse("rest_friendship:api-root", request=request, format=format),
        # "core": reverse("core-root", request=request, format=format),
        "obtain api token auth": reverse("api-token", request=request, format=format),
        "refresh api token auth": reverse("refresh-api-token", request=request, format=format),
        "verify token auth": reverse("verify-api-token", request=request, format=format),
        # "documents": reverse("drfdocs", request=request, format=format),
        "accounts": reverse("rest-auth-root", request=request, format=format)
    })


@api_view(('GET', ))
@permission_classes((permissions.AllowAny,))
def api_rest_auth(request, format=None):
    return Response({
        "user": reverse("rest-auth:rest_user_details", request=request, format=format),
        "login": reverse("rest-auth:rest_login", request=request, format=format),
        "logout": reverse("rest-auth:rest_logout", request=request, format=format),
        "registration": reverse("rest_register", request=request, format=format),
    })


@api_view(('GET', ))
@permission_classes((permissions.AllowAny,))
def api_core(request, format=None):
    return Response({
        # "core": reverse("v1:core-url:api-root", request=request, format=format),
        "profile": reverse("v1:core-url:core_profile_detail", request=request, format=format),
        "search": os.path.join(reverse("v1:core-url:core_profile_detail", request=request, format=format), 'search'),
        "firebase-token": reverse("v1:core-url:core_firebase_token", request=request, format=format)
        # "role": reverse("core:core_role_detail", request=request, format=format)
    })


@api_view(('GET', ))
@permission_classes((permissions.AllowAny,))
def api_v1_root(request, format=None):
    return Response({
        "core": reverse("v1:v1-core", request=request, format=format),
        "classroom": reverse("v1:classroom:api-root", request=request, format=format),
        "writing": reverse("v1:writing:api-root", request=request, format=format)
        # "problem": reverse("v1:problem:api-root", request=request, format=format),
        # "math": reverse("v1:math:api-root", request=request, format=format),
        # "reading": reverse("v1:reading:api-root", request=request, format=format),
        # "topic": reverse("v1:topic:api-root", request=request, format=format)
    })


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = SchemaGenerator(title='Spiral API')
    return Response(generator.get_schema(request=request))