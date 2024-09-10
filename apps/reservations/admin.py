from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
  list_display = ('reservation_name', 'service', 'status', 'booking_date', 'number_of_people')
  list_filter = ('status', 'service')
  search_fields = ('reservation_name', 'service__title')
  readonly_fields = ('id',)
  fieldsets = (
    (None, {
      'fields': ('id', 'reservation_name', 'service', 'user')
    }),
    ('Reservation Details', {
      'fields': ('status', 'number_of_people', 'booking_date', 'length_of_stay')
    }),
  )