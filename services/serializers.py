from rest_framework.serializers import ModelSerializer
from .models import CloudServiceCategory,CloudService

class CloudServiceCategorySerializer(ModelSerializer):
    class Meta:
        model = CloudServiceCategory
        fields = "__all__"

class CloudServiceSerializer(ModelSerializer):
    class Meta:
        model = CloudService
        fields = ['name','description']