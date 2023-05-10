from django.db import models

class CloudService(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('CloudServiceCategory',on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class CloudServiceCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

