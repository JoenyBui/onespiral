from rest_framework_extensions.routers import ExtendedDefaultRouter

from writing import viewsets

router = ExtendedDefaultRouter()

router.register(r'document/search', viewsets.DocumentSearchViewSet, base_name='document-search')

document_router = router.register(r'document', viewsets.DocumentModelViewSet, 'document')
document_router.register(r'shared',
                         viewsets.DocumentLinkModelViewSet,
                         base_name='document-shared',
                         parents_query_lookups=['doc__uuid'])

writer_router = router.register(r'writer', viewsets.WriterModelViewSet, 'writer')
writer_router.register(r'document',
                       viewsets.DocumentModelViewSet,
                       base_name='writer-document',
                       parents_query_lookups=['writer__user__profile__uuid'])
writer_router.register(r'shared',
                       viewsets.SharedDocumentLinkViewSet,
                       base_name='writer-shared-document',
                       parents_query_lookups=['to_user__user__profile__uuid'])


router.register(r'shared-document', viewsets.SharedDocumentLinkViewSet, base_name='shared-document-link')