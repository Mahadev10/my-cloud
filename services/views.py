from django.shortcuts import render
from rest_framework import generics
from .models import CloudServiceCategory,CloudService
from .serializers import CloudServiceCategorySerializer,CloudServiceSerializer
class CloudServiceCategoryList(generics.ListCreateAPIView):
    queryset = CloudServiceCategory.objects.all()
    serializer_class = CloudServiceCategorySerializer

class  CloudServiceCategoryDetail(generics.UpdateAPIView):
    queryset =  CloudServiceCategory.objects.all()
    serializer_class =  CloudServiceCategorySerializer


class CloudServiceList(generics.ListCreateAPIView):
    serializer_class = CloudServiceSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        services = CloudService.objects.filter(category=id)
        return services
    def perform_create(self,serializer):
        print(serializer)
        category=CloudServiceCategory(id=self.kwargs['id'])
        serializer.save(category=category)

class  CloudServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =  CloudServiceSerializer
    def get_object(self):
        category_id=self.kwargs['id']
        service_id=self.kwargs['pk']
        service = CloudService.objects.get(category=category_id,pk=service_id)
        return service