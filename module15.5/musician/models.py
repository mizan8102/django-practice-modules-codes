from django.db import models

# Create your models here.
class MusicianModel(models.Model):
  first_name= models.CharField(max_length=250)
  last_name = models.CharField(max_length=250)
  email = models.EmailField()
  phone_number = models.IntegerField()
  instrument_type= models.CharField(max_length=250)
  
  def __str__(self) -> str:
    return self.first_name+" "+self.last_name