from django.conf.urls import include, url

from classroom.routers import router as classroom_router
from writing.routers import router as writing_router
# from core.routers import router as core_router

__author__ = 'jbui'


urlpatterns = [
    url(r'^classroom/', include(classroom_router.urls, namespace='classroom')),
    url(r'^writing/', include(writing_router.urls, namespace='writing'))
]
