from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import *


# Project Pagination:
class ProjectPagination(PageNumberPagination):   # always used in List!
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000


# Project CRUD:
@extend_schema_view(
    list=extend_schema(summary='List Project', tags=['Project']),
    retrieve=extend_schema(summary='Retrieve Project', tags=['Project']))
class RLProject(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    serializer_class = ProjectSerializers
    queryset = Project.objects.all()
    pagination_class = ProjectPagination
    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
    )
    search_fields = ['title']

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Project.objects.all()

        return Project.objects.filter(pk=pk)


# Category CRUD:
@extend_schema_view(
    list=extend_schema(summary='List Category', tags=['Category']),
    retrieve=extend_schema(summary='Retrieve Category', tags=['Category']),
    create=extend_schema(summary='create Category', tags=['Category']),
    update=extend_schema(summary='update Category', tags=['Category']),
    partial_update=extend_schema(summary='partial_update Category', tags=['Category']),
    destroy=extend_schema(summary='destroy Category', tags=['Category'])
)
class CRUDCategory(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = CategorySerializers
    pagination_class = ProjectPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Category.objects.all()

        return Category.objects.filter(pk=pk)



# Project Details CRUD:
@extend_schema_view(
    list=extend_schema(summary='List Project Details', tags=['Project Details']),
    retrieve=extend_schema(summary='Retrieve Project Details', tags=['Project Details']),
    create=extend_schema(summary='create Project Details', tags=['Project Details']),
    update=extend_schema(summary='update Project Details', tags=['Project Details']),
    partial_update=extend_schema(summary='partial_update Project Details', tags=['Project Details']),
    destroy=extend_schema(summary='destroy Project Details', tags=['Project Details']
))
class CRUDProjectDetails(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = ProjectDetailsSerializers
    pagination_class = ProjectPagination
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Project.objects.all()

        return Project.objects.filter(pk=pk)



# Project Showcase CRUD:
@extend_schema_view(
    list=extend_schema(summary='List Project Showcase', tags=['Project Showcase']),
    retrieve=extend_schema(summary='Retrieve Project Showcase', tags=['Project Showcase'])
)
class ProjectShowcase(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = ProjectSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title']
    pagination_class = ProjectPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Project.objects.all()

        return Project.objects.filter(pk=pk)




# Upload image CRUD:
@extend_schema_view(
    create=extend_schema(summary='create Upload Image', tags=['Upload Image'])
)

class UploadImage(mixins.CreateModelMixin,
                   GenericViewSet):
    serializer_class = UploadSerializers
    queryset = Upload.objects.all()
