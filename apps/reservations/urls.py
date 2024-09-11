from django.urls import path
from apps.reservations.views import ReserveUsers

urlpatterns = [
  path('reserve/', ReserveUsers.as_view(), name='reserve-user'),
]