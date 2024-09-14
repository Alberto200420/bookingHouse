from django.db import models
import uuid
from apps.serviceDirectory.models import Service
from apps.users.models import UserAccount

class Reservation(models.Model):
  STATUS_CHOICES = [
    ('RESERVED', 'Reserved'),
    ('CANCELLED', 'Cancelled'),
    ('COMPLETED', 'Completed'),
  ]

  id =                models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  service =           models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reservations')
  number_of_people =  models.PositiveSmallIntegerField()
  status =            models.CharField(max_length=9, choices=STATUS_CHOICES, default='RESERVED')
  booking_date =      models.DateTimeField()
  arrival_time =      models.TimeField(blank=True, null=True)
  departure_time =    models.TimeField(blank=True, null=True)
  user =              models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING, related_name='services')

  def __str__(self):
    return f"Reservation for {self.user.first_name, self.user.last_name} - {self.service.title}"

  class Meta:
    ordering = ['-booking_date']