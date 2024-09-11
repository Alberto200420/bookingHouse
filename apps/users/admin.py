from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.hotels.models import Hotel
from .models import UserAccount

class UserAccountAdmin(UserAdmin):
  list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'hotel_belonging')
  list_filter = ('is_active', 'is_staff', 'is_superuser', 'hotel_belonging')
  search_fields = ('email', 'first_name', 'last_name', 'hotel_belonging__hotel_name')
  readonly_fields = ('id',)
  ordering = ('email',)
    
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal Info', {'fields': ('first_name', 'last_name')}),
    ('Hotel Association', {'fields': ('hotel_belonging',)}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    ('Important dates', {'fields': ('last_login',)}),
  )
    
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'first_name', 'last_name', 'hotel_belonging', 'password1', 'password2'),
    }),
  )

  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    if db_field.name == "hotel_belonging":
      kwargs["queryset"] = Hotel.objects.all().order_by('hotel_name')
    return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(UserAccount, UserAccountAdmin)