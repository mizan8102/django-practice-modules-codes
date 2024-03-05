from django.db import models
from musician.models import MusicianModel
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=255)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    album_release_date = models.DateField(default=timezone.now)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


    def __str__(self) -> str:
        return self.album_name
