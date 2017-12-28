from rest_framework_extensions.routers import ExtendedDefaultRouter

from writing import viewsets

router = ExtendedDefaultRouter()

router.register(r'document/search', viewsets.DocumentSearchViewSet, base_name='document-search')
document_router = router.register(r'document', viewsets.DocumentModelViewSet, 'document')

writer_router = router.register(r'writer', viewsets.WriterModelViewSet, 'writer')
writer_router.register(r'document',
                        viewsets.DocumentModelViewSet,
                        base_name='writer-document',
                        parents_query_lookups=['writer'])

