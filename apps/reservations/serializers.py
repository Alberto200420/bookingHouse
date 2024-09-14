from rest_framework import serializers
from apps.reservations.models import Reservation
from apps.serviceDirectory.models import Service
from django.utils import timezone

class ReservationCreateSerializer(serializers.ModelSerializer):
  service = serializers.UUIDField()  # Expecting service ID to be passed as a UUID

  class Meta:
    model = Reservation
    fields = ['service', 'number_of_people', 'booking_date']

  def validate_service(self, value):
    # Ensure the service exists
    try:
      service = Service.objects.get(id=value)
    except Service.DoesNotExist:
      raise serializers.ValidationError("Service does not exist.")
    return service

  def validate_booking_date(self, value):
    if value < timezone.now():
      raise serializers.ValidationError("Booking date cannot be in the past.")
    return value

  def create(self, validated_data):
    user = self.context['request'].user
    service = validated_data.pop('service')
        
    # Create and return the reservation
    reservation = Reservation.objects.create(user=user, service=service, **validated_data)
    return reservation