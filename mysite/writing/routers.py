from rest_framework_extensions.routers import ExtendedDefaultRouter

from writing import viewsets

router = ExtendedDefaultRouter()

document_router = router.register(r'document', viewsets.DocumentModelViewSet, 'document')

writer_router = router.register(r'writer', viewsets.WriterModelViewSet, 'writer')
writer_router.register(r'document',
                        viewsets.DocumentModelViewSet,
                        base_name='writer-document',
                        parents_query_lookups=['writer'])
