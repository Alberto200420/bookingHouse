from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/auth/", include('djoser.urls')),
    path("v1/auth/", include('djoser.urls.jwt')),
    path("v1/directory/", include('apps.serviceDirectory.urls')),
    path("v1/reservations/", include('apps.reservations.urls')),
    path("v1/hotel/", include('apps.hotels.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)