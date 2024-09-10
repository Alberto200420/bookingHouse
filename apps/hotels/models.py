from django.db import models

def logo_directory(instace, filename):
  return 'logos/{0}/{1}'.format(instace.hotel_name, filename)

class Hotel(models.Model):
  hotel_name = models.CharField(max_length=100, unique=True, editable=True)
  logo =       models.ImageField(upload_to=logo_directory)

  def __str__(self):
    return self.hotel_name