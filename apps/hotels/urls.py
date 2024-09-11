from django.urls import path
from .views import *

urlpatterns = [
  path('get/<str:hotel_name>/', GetHotelHomePage.as_view(), name='hotel-home-page'),
]