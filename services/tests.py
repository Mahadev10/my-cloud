from rest_framework.test import APITestCase
from .models import CloudService,CloudServiceCategory


class ServiceCategoryTest(APITestCase):
    def test_get_all_service_categories(self):
        response = self.client.get(f'/services-categories/')
        self.assertEqual(response.status_code, 200)
    def test_create_service_category(self):
        data={"name": "database"}
        response = self.client.post('/services-categories/',data)
        self.assertEqual(response.status_code, 201)
    def test_update_service_category(self):
        obj=CloudServiceCategory.objects.create(name="database")
        id=obj.id
        data={"name": "databases"}
        response = self.client.put(f'/services-categories/{id}',data)
        self.assertEqual(response.status_code, 200)
    def test_delete_service_category(self):
        obj=CloudServiceCategory.objects.create(name="database")
        id=obj.id
        response = self.client.delete(f'/services-categories/{id}')
        self.assertEqual(response.status_code, 204)

class ServiceTest(APITestCase):
    def test_get_all_services(self):
        response = self.client.get(f'/services-categories/1/services/')
        self.assertEqual(response.status_code, 200)
    def test_create_service(self):
        obj=CloudServiceCategory.objects.create(name="Compute")
        id=obj.id
        data={"name": "Lambda", "description": "Serverless Computing"}
        response = self.client.post('/services-categories/1/services/',data)
        self.assertEqual(response.status_code, 201)
    def test_update_service(self):
        category=CloudServiceCategory.objects.create(name="Compute")
        service=CloudService.objects.create(name="Lambda",description="Serverless Computing",category=category)
        data={"name": "EC2","description": "Elastic Cloud Computing"}
        response = self.client.put(f'/services-categories/{category.id}/services/{service.id}',data)
        self.assertEqual(response.status_code, 200)
    def test_delete_service_category(self):
        category=CloudServiceCategory.objects.create(name="Compute")
        service=CloudService.objects.create(name="Lambda",description="Serverless Computing",category=category)
        response = self.client.delete(f'/services-categories/{category.id}/services/{service.id}')
        self.assertEqual(response.status_code, 204)