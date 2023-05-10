from django.urls import path
from . import views
urlpatterns = [
path('services-categories/',views.CloudServiceCategoryList.as_view()),
path('services-categories/<int:pk>',views.CloudServiceCategoryDetail.as_view()),
path('services-categories/<int:id>/services/',views.CloudServiceList.as_view()),
path('services-categories/<int:id>/services/<int:pk>',views.CloudServiceDetail.as_view()),
]