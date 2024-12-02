from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.SimpleRouter()
router.register(r'crudcompany', CRUDCompany, basename='company')
router.register(r'crudteammember', CRUDTeammember, basename='teammember')

urlpatterns = [
    path('about/', include(router.urls)),
]
