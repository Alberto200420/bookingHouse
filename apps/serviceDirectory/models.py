from django.db import models
from apps.hotels.models import Hotel
import uuid
# Cambiar path para que se vea /nombre del hotel/service/etc
def header_service_directory(instace, filename):
  return 'service/{0}/{1}'.format(instace.title, filename)

def menu_service_directory(instace, filename):
  return 'service/{0}/menu/{1}'.format(instace.title, filename)

def header_images_directory(instace, filename):
  return 'service/{0}/images/{1}'.format(instace.service.title, filename)

def category_image_directory(instace, filename):
  return 'logos/{0}/category/{1}'.format(instace.hotel.hotel_name, filename)

class Category(models.Model):
  id =            models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  hotel =         models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel')
  image_display = models.ImageField(upload_to=category_image_directory)
  category_name = models.CharField(max_length=80)

  def __str__(self):
    return f"{self.hotel} - {self.category_name}"

class Service(models.Model):
  id =                  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  category =            models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category')
  title =               models.CharField(max_length=100)
  menu =                models.FileField(upload_to=menu_service_directory, blank=True, null=True)
  header_image =        models.ImageField(upload_to=header_service_directory)
  description =         models.TextField()
  availabilities =      models.JSONField()
  requirement =         models.TextField(blank=True, null=True)
  require_reservation = models.BooleanField(default=False)
  maximum_capacity =    models.PositiveSmallIntegerField(blank=True, null=True)

  def __str__(self):
    return self.title

class Images(models.Model):
  service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
  description = models.CharField(max_length=50)
  image = models.ImageField(upload_to=header_images_directory)

  def __str__(self):
    return f"Image for {self.service.title}: {self.description}"