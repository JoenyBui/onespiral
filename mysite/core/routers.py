from rest_framework_extensions.routers import ExtendedDefaultRouter

# from rest_framework_friendship import views
from core import viewsets as core_viewsets
from writing import viewsets as writing_viewsets
from rest_friendship import viewsets as friendship_viewsets

router = ExtendedDefaultRouter()

router.register(r'profile/search', core_viewsets.ProfileSearchViewSet, base_name='profile-search')
# profile_router = router.register(r'profile', viewsets.ProfileDetailViewSets, 'profile')

me_router = router.register(r'me', writing_viewsets.MeWriterModelViewSet, base_name='me')
me_router.register(r'document',
                   writing_viewsets.DocumentModelViewSet,
                   base_name='me-writer-document',
                   parents_query_lookups=['writer__user__profile__uuid'])
me_router.register(r'shared',
                   writing_viewsets.SharedDocumentLinkViewSet,
                   base_name='me-writer-shared-document',
                   parents_query_lookups=['to_user__user__profile__uuid'])
me_router.register(r'friend',
                   friendship_viewsets.FriendsModelViewSets,
                   base_name='me-friends',
                   parents_query_lookups=['profile__uuid'])
