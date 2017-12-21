from django.conf.urls import include, url

from ..view import api_root, api_v1_root, api_rest_auth

urlpatterns = [
    url(r'^$', api_root, name='api-index'),
    url(r'^rest-auth/$', api_rest_auth, name='rest-auth-root'),
    url(r'^rest-auth/', include('rest_auth.urls', namespace='rest-auth')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^core/', include('core.urls'), name='core'),
    url(r'^v1/$', api_v1_root, name='v1-root'),
    url(r'^v1/', include('mysite.api.v1', namespace='v1'))
]