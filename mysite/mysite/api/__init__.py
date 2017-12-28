from django.conf.urls import include, url

from ..view import api_root, api_v1_root, api_rest_auth, api_core

from rest_friendship.routers import router

from rest_framework.authtoken import views as restful_view
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
    # API Browsing View
    url(r'^$', api_root, name='api-index'),

    # Search and Friendship
    url(r'^search/', include('haystack.urls')),
    url(r'^friendship/', include(router.urls, namespace='rest_friendship')),

    # Authentication
    url(r'^rest-auth/$', api_rest_auth, name='rest-auth-root'),
    url(r'^rest-auth/', include('rest_auth.urls', namespace="rest-auth")),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    url(r'^api-token-auth/', obtain_jwt_token, name="api-token"),
    url(r'^api-token-refresh/', refresh_jwt_token, name='refresh-api-token'),
    url(r'^api-token-verify/', verify_jwt_token, name='verify-api-token'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Core
    url(r'core/$', api_core, name='core-root'),
    url(r'^core/', include('core.urls', namespace='core')),

    # API Version
    url(r'^v1/$', api_v1_root, name='v1-root'),
    url(r'^v1/', include('mysite.api.v1', namespace='v1'))
]