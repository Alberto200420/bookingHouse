from rest_framework import serializers
from .models import Hotel

class GetHotelHomePageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hotel
    fields = '__all__'