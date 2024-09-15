from rest_framework import serializers
from .models import Service, Category, Images
from datetime import datetime

class ImagesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Images
    fields = ['description', 'image']


class ServiceSerializer(serializers.ModelSerializer):
  images = ImagesSerializer(many=True, read_only=True)  # Add the images field

  class Meta:
    model = Service
    fields = [
      'id', 'category', 'title', 'menu', 'header_image', 'description', 
      'availabilities', 'requirement', 'require_reservation', 'maximum_capacity', 'images',
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
    fields = ['image_display', 'category_name', 'services']
