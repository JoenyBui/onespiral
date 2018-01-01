from rest_framework_extensions.routers import ExtendedDefaultRouter

from mysite import viewsets as mysite_viewsets
from writing import viewsets as writing_viewsets
from rest_friendship import viewsets as friendship_viewsets

me_router = ExtendedDefaultRouter()
me_router.register(r'document',
                   mysite_viewsets.MeDocumentViewSet,
                   base_name='me-writer-document')
me_router.register(r'shared',
                   mysite_viewsets.MeSharedDocumentModelViewSet,
                   base_name='me-writer-shared-document')
me_router.register(r'friend',
                   mysite_viewsets.MeFriendModelViewSet,
                   base_name='me-friends')
me_router.register(r'friendship-to-user',
                   mysite_viewsets.MeFriendshipToUserModelViewSets,
                   base_name='me-friendship-to-user')
me_router.register(r'friendship-from-user',
                   mysite_viewsets.MeFriendshipFromUserModelViewSets,
                   base_name='me-friendship-from-user')
me_router.register(r'friendship-request-to-user',
                   mysite_viewsets.MeFriendshipToUserRequestViewSet,
                   base_name='me-friendship-request-to-user')
me_router.register(r'friendship-request-from-user',
                   mysite_viewsets.MeFriendshipFromUserRequestViewSet,
                   base_name='me-friendship-request-from-user')
me_router.register(r'follower',
                   mysite_viewsets.MeFollowFollowerModelViewSet,
                   base_name='me-follower')
me_router.register(r'followee',
                   mysite_viewsets.MeFollowFolloweeModelViewSet,
                   base_name='me-followee')
