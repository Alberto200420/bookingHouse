from rest_framework import serializers
from .models import Service, Category
from datetime import datetime

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = [
      'id', 'category', 'title', 'menu', 'header_image', 'description', 
      'availabilities', 'requirement', 'require_reservation', 'maximum_capacity'
    ]

class TodayServiceSerializer(serializers.ModelSerializer):
  availabilities = serializers.SerializerMethodField()

  class Meta:
    model = Service
    fields = ['id', 'title', 'header_image', 'availabilities', 'require_reservation']

  def get_availabilities(self, obj):
    today = self.context.get('today')
    current_time = datetime.now().time()

    # Fetch today's available times
    availabilities = obj.availabilities.get(today, {}).get('availableTimes', [])

    # Filter out times that are earlier than the current time
    future_times = [time for time in availabilities if datetime.strptime(time, '%H:%M:%S').time() > current_time]
    return future_times


class ServiceListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = ['id', 'title', 'header_image', 'require_reservation']

class CategorySerializer(serializers.ModelSerializer):
  services = ServiceListSerializer(many=True, read_only=True, source='category')

  class Meta:
    model = Category
    fields = ['category_name', 'services']
