from django.urls import path
from .views import *

urlpatterns = [
  path('services/today/', GetTodayServices.as_view(), name='today-services'),
  path('categories/services/', GetCategory_and_ServiceList.as_view(), name='category-service-list'),
  path('service/<uuid:service_id>/', GetService.as_view(), name='service-detail'),
]