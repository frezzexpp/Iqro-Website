from rest_framework import serializers
from .models import Contact


# Contact Serializer:
class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"