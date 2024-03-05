from .models import AlbumModel
from django import forms


class AlbumForm(forms.ModelForm):
  class Meta:
    model = AlbumModel
    fields = '__all__'
