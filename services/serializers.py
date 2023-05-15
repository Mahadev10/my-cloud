from rest_framework.serializers import ModelSerializer
from .models import CloudServiceCategory,CloudService,Attribute

class CloudServiceCategorySerializer(ModelSerializer):
    class Meta:
        model = CloudServiceCategory
        fields = "__all__"

class AttributeSerializer(ModelSerializer):
    class Meta:
        model = Attribute
        fields= ['key','value']

class CloudServiceSerializer(ModelSerializer):
    attributes = AttributeSerializer(read_only=True,many=True)
    class Meta:
        model = CloudService
        fields = ['id','name','description','attributes']