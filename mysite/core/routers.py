from rest_framework_extensions.routers import ExtendedDefaultRouter

# from rest_framework_friendship import views
from . import viewsets

router = ExtendedDefaultRouter()

router.register(r'profile', viewsets.ProfileDetailViewSets, 'profiles')
# router.register(r'role', viewsets.UserRoleDetailViewSet, 'roles')
