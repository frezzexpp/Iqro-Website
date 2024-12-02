from rest_framework import mixins, status
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import *



# Contact Pagination:
class ContactPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000



# Contact CRUD:
@extend_schema_view(
    list=extend_schema(summary='list contact project', tags=['Contact']),
    retrieve=extend_schema(summary='retrieve contact project', tags=['Contact']),
    create=extend_schema(summary='create contact project', tags=['Contact']),
    destroy=extend_schema(summary='destroy contact project', tags=['Contact']
))

class CRUDContact(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    pagination_class = ContactPagination
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'phone']

