from django.urls import path, include
from rest_framework import routers

from project.views import *

router = routers.SimpleRouter()
router.register(r'crudproject', RLProject, basename='project')
router.register(r'crudcategory', CRUDCategory, basename='categoryproject')
router.register(r'crudprojectdetails', CRUDProjectDetails, basename='projectdetails')
router.register(r'crudprojectshowcase', ProjectShowcase, basename='projectshowcase')

urlpatterns = [
    path('project/', include(router.urls)),
]
