from django.conf.urls import include, url

from classroom.routers import router as classroom_router
from writing.routers import router as writing_router
from rest_friendship.routers import router as friend_router

from ..view import api_core
# from core.routers import router as core_router

__author__ = 'jbui'


urlpatterns = [
    url(r'^classroom/', include(classroom_router.urls, namespace='classroom')),
    url(r'^writing/', include(writing_router.urls, namespace='writing')),
    url(r'^friendship/', include(friend_router.urls, namespace='rest_friendship')),

    url(r'^core/$', api_core, name='v1-core'),
    url(r'^core/', include('core.urls', namespace='core-url'))
]
