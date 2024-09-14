from django.contrib import admin
from .models import Reservation
from apps.serviceDirectory.models import Service
from apps.users.models import UserAccount

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
  list_display = ('user__first_name', 'service', 'status', 'booking_date', 'number_of_people', 'arrival_time', 'departure_time')
  list_filter = ('status', 'service', 'booking_date')
  search_fields = ('id', 'service__title', 'user__email')
  readonly_fields = ('id',)
    
  fieldsets = (
    (None, {
      'fields': ('id', 'service', 'user')
    }),
    ('Reservation Details', {
      'fields': ('status', 'number_of_people', 'booking_date', 'arrival_time', 'departure_time')
    }),
  )

  def get_queryset(self, request):
    queryset = super().get_queryset(request)
    return queryset.select_related('service', 'user')

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == "service":
      kwargs["queryset"] = Service.objects.all().order_by('title')
    elif db_field.name == "user":
      kwargs["queryset"] = UserAccount.objects.all().order_by('email')
    return super().formfield_for_foreignkey(db_field, request, **kwargs)