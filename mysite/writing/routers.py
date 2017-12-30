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


me_router = router.register(r'me', viewsets.MeWriterModelViewSet, base_name='me-writer')
me_router.register(r'document',
                   viewsets.DocumentModelViewSet,
                   base_name='me-writer-document',
                   parents_query_lookups=['writer__user__profile__uuid'])
