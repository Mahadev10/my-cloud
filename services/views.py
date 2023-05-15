from django.shortcuts import render
from rest_framework import generics
from .models import CloudServiceCategory,CloudService,Attribute
from .serializers import CloudServiceCategorySerializer,CloudServiceSerializer,AttributeSerializer
class CloudServiceCategoryList(generics.ListCreateAPIView):
    queryset = CloudServiceCategory.objects.all()
    serializer_class = CloudServiceCategorySerializer

class  CloudServiceCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
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

class AttributeList(generics.ListCreateAPIView):
    serializer_class = AttributeSerializer
    def get_queryset(self):
        category_id=self.kwargs['id']
        service_id=self.kwargs['pk']
        service = CloudService.objects.get(category=category_id,pk=service_id)
        attributes = Attribute.objects.filter(service=service)
        return attributes
    def perform_create(self,serializer):
        category_id=self.kwargs['id']
        service_id=self.kwargs['pk']
        service = CloudService.objects.get(category=category_id,pk=service_id)
        serializer.save(service=service)

class  AttributeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =  AttributeSerializer
    def get_object(self):
        category_id=self.kwargs['id']
        service_id=self.kwargs['pk']
        attr_id = self.kwargs['attr_id']
        service = CloudService.objects.get(category=category_id,pk=service_id)
        attribute = Attribute.objects.get(service=service,id=attr_id)
        return attribute