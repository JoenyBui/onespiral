from rest_framework_extensions.routers import ExtendedDefaultRouter

# from rest_framework_friendship import views
from . import viewsets

router = ExtendedDefaultRouter()

router.register(r'profile/search', viewsets.ProfileSearchViewSet, base_name='profile-search')
# profile_router = router.register(r'profile', viewsets.ProfileDetailViewSets, 'profile')
