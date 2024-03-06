from .models import AlbumModel
from django import forms


class AlbumForm(forms.ModelForm):
  class Meta:
    model = AlbumModel
    fields = '__all__'
    widgets = {
        'album_release_date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'})
      }
