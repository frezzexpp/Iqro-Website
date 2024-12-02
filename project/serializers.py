from rest_framework import serializers

from project.models import Project, Category, Upload


#Project
class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'image', 'title', 'description']


#Project Details
class ProjectDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'




class UploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ('image', )


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"