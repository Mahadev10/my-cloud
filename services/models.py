from django.db import models


class Attribute(models.Model):
    key=models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    service=models.ForeignKey('CloudService',on_delete=models.CASCADE,related_name='attributes')
    class Meta:
        unique_together = ('key','value','service')
    def __str__(self):
        return f'{self.key}-{self.value}'
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

