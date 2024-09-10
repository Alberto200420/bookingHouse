from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount

class UserAccountAdmin(UserAdmin):
  list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
  list_filter = ('is_active', 'is_staff', 'is_superuser')
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email',)
    
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal Info', {'fields': ('first_name', 'last_name')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    ('Important dates', {'fields': ('last_login',)}),
  )
    
  add_fieldsets = (
    (None, {
      'classes': ('wide',),
      'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
    }),
  )

admin.site.register(UserAccount, UserAccountAdmin)