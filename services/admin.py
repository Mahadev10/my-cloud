from django.contrib import admin
from . import models

admin.site.register(models.CloudService)
admin.site.register(models.Attribute)
admin.site.register(models.CloudServiceCategory)