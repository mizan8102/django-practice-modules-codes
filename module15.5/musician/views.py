from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import MusicianModel
# Create your views here.

def addMusician(request):
  if request.method == 'POST':
    form= MusicianForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('addMusician')

  form = MusicianForm()
  return render(request, 'musician/add_musician.html', { 'form' : form})


# edit musician 
def editMusician(request, id):
  return "hdlj"
  

# list of musician 
def list_musician(request):
  musician_lists = MusicianModel.objects.all()
  return render(request, 'musician/list_musician.html', { 'data' : musician_lists})