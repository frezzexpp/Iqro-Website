from django.urls import path, include
from rest_framework import routers
from contact.views import *

router = routers.SimpleRouter()
router.register(r'listcontact', CRUDContact, basename='contact')
urlpatterns = [
    path('contact/', include(router.urls)),
]