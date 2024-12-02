from drf_spectacular.utils import extend_schema_view, extend_schema
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import *



# about app pagination setting:
class AboutPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000




# Company CRUD:
@extend_schema_view(
    list=extend_schema(summary='list companyinfo', tags=['Company']),
    retrieve=extend_schema(summary='retrive companyinfo', tags=['Company']),
    create=extend_schema(summary='create companyinfo', tags=['Company']),
    update=extend_schema(summary='update companyinfo', tags=['Company']),
    partial_update=extend_schema(summary='partial_update companyinfo', tags=['Company']),
    destroy=extend_schema(summary='destroy companyinfo', tags=['Company']
))
class CRUDCompany(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = CompanyInfoSerializer
    pagination_class = AboutPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return CompanyInfo.objects.all()

        return CompanyInfo.objects.filter(pk=pk)




# Team CRUD:
@extend_schema_view(
    list=extend_schema(summary='list team members', tags=['Teammember']),
    retrieve=extend_schema(summary='retrieve team member', tags=['Teammember']),
    create=extend_schema(summary='create team members', tags=['Teammember']),
    update=extend_schema(summary='update team members', tags=['Teammember']),
    partial_update=extend_schema(summary='partial_update team members', tags=['Teammember']),
    destroy=extend_schema(summary='destroy team members', tags=['Teammember']
))
class CRUDTeammember(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = TeamMemberSerializer
    pagination_class = AboutPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']



    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return TeamMember.objects.all()
        return TeamMember.objects.filter(pk=pk)