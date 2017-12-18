from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^students/$', views.StudentListView.as_view(), name='students'),
    url(r'^student/(?P<pk>\d+)$', views.StudentDetailView.as_view(), name='studemt-detail'),
]
