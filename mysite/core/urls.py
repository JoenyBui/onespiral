from django.conf.urls import url, include

from .viewsets import ProfileDetailViewSets
from .views import get_firebase_minted_token

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^profile/$', ProfileDetailViewSets.as_view(), name='core_profile_detail'),
    url(r'^firebase-token/$', get_firebase_minted_token, name='core_firebase_token')
    # url(r'^friendship/%', include(router.urls, namespace='friendship'))
]
