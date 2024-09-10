from django.contrib import admin
from .models import Category, Service, Images

class ImagesInline(admin.TabularInline):
  model = Images
  extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('category_name', 'hotel')
  list_filter = ('hotel',)
  search_fields = ('category_name', 'hotel__hotel_name')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  list_display = ('title', 'category', 'require_reservation', 'maximum_capacity')
  list_filter = ('category', 'require_reservation')
  search_fields = ('title', 'description')
  inlines = [ImagesInline]
  fieldsets = (
    (None, {
      'fields': ('title', 'category', 'description')
    }),
    ('Media', {
      'fields': ('menu', 'header_image')
    }),
    ('Availability', {
      'fields': ('availabilities', 'require_reservation', 'maximum_capacity')
    }),
    ('Additional Info', {
      'fields': ('requirement',),
      'classes': ('collapse',)
    }),
  )

# We don't register Images model separately as it's managed inline with Service