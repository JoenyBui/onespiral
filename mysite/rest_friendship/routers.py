from .viewsets import FriendsModelViewSets, FriendshipModelViewSets, FriendshipRequestViewSet, FollowModelViewSet

from rest_framework_extensions.routers import ExtendedDefaultRouter


router = ExtendedDefaultRouter()
router.register(r'friends', FriendsModelViewSets, base_name='friends')
router.register(r'friendship', FriendshipModelViewSets, base_name='friendship')
router.register(r'friendrequests', FriendshipRequestViewSet, base_name='friendrequests')
router.register(r'follow', FollowModelViewSet, base_name='follow')
