from django.urls import path, include
from rest_framework import routers
from .views import CRUDService, CRUDIdeas, CRUDProcessStep


router = routers.SimpleRouter()
router.register(r'crudservice', CRUDService, basename="servicehomepage")
router.register(r'crudideas', CRUDIdeas, basename="ideashomepage")
router.register(r'crudprocessstep', CRUDProcessStep, basename="processstephomepage")
url_patterns = [
    path('service/', include(router.urls))
]


