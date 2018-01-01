from rest_framework_extensions.routers import ExtendedDefaultRouter

# from rest_framework_friendship import views
from core import viewsets as core_viewsets
from writing import viewsets as writing_viewsets
from rest_friendship import viewsets as friendship_viewsets

router = ExtendedDefaultRouter()

router.register(r'profile/search', core_viewsets.ProfileSearchViewSet, base_name='profile-search')
# profile_router = router.register(r'profile', viewsets.ProfileDetailViewSets, 'profile')

# me1_router = router.register('friendship', friendship_viewsets.FriendshipViewSet,base_name='my_friendship')
# me_router = router.register(r'me', core_viewsets.MeProfileModelViewSets, base_name='me')
# me_router = router.register(r'me', writing_viewsets.MeWriterModelViewSet, base_name='me')
# me_router.register(r'writer', writing_viewsets.MeWriterModelViewSet, base_name='me-writer', parents_query_lookups='user__profile__uuid')
