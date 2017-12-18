from django.conf.urls import include, url

from ..view import api_root, api_v1_root

urlpatterns = [
    url(r'^$', api_root, name='api-index'),
    url(r'^v1/$', api_v1_root, name='v1-root'),
    url(r'^v1/', include('mysite.api.v1', namespace='v1'))
]