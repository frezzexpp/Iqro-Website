from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from homepage.models import Service, ProcessStep, Ideas
from homepage.serializers import *



# Homepage pagination:
class HomepagePagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000



# Service CRUD:
@extend_schema_view(
    list=extend_schema(summary='list service', tags=['Service']),
    retrieve=extend_schema(summary='retrieve service', tags=['Service']),
    create=extend_schema(summary='create service', tags=['Service']),
    update=extend_schema(summary='update service', tags=['Service']),
    partial_update=extend_schema(summary='partial_update service', tags=['Service']),
    destroy=extend_schema(summary='destroy service', tags=['Service'])
)
class CRUDService(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializers
    pagination_class = HomepagePagination
    filter_backends = [SearchFilter]
    search_fields = ['title']



# Ideas CRUD:
@extend_schema_view(
    list=extend_schema(summary='list ideas', tags=['Ideas']),
    retrieve=extend_schema(summary='retrieve ideas', tags=['Ideas']),
    create=extend_schema(summary='create ideas', tags=['Ideas']),
    update=extend_schema(summary='update ideas', tags=['Ideas']),
    partial_update=extend_schema(summary='partial_update ideas', tags=['Ideas']),
    destroy=extend_schema(summary='destroy ideas', tags=['Ideas'])
)
class CRUDIdeas(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Ideas.objects.all()
    serializer_class = IdeasSerializers
    pagination_class = HomepagePagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'role']



# Process CRUD:
@extend_schema_view(
    list=extend_schema(summary='list processstep', tags=['ProcessStep']),
    retrieve=extend_schema(summary='retrieve processstep', tags=['ProcessStep']),
    create=extend_schema(summary='create processstep', tags=['ProcessStep']),
    update=extend_schema(summary='update processstep', tags=['ProcessStep']),
    partial_update=extend_schema(summary='partial_update processstep', tags=['ProcessStep']),
    destroy=extend_schema(summary='destroy processstep', tags=['ProcessStep'])
)
class CRUDProcessStep(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = ProcessStep.objects.all()
    serializer_class = ProcessStepSerializers
    filter_backends = [SearchFilter]
    pagination_class = HomepagePagination
    search_fields = ['title']