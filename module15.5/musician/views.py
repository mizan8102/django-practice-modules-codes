from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicianForm
from .models import MusicianModel

# Create your views here.

# add musician 
def addMusician(request):
  if request.method == 'POST':
    form= MusicianForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('view_musician_list')

  form = MusicianForm()
  return render(request, 'musician/add_musician.html', { 'form' : form})


# edit musician 
def editMusician(request, id):
    musician = get_object_or_404(MusicianModel, pk=id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('view_musician_list')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'musician/add_musician.html', {'form': form})


#delete musician 
def deleteMusician(request, id):
  musician = MusicianModel.objects.get(pk=id) 
  musician.delete()
  return redirect('view_musician_list')
  

# list of musician 
def list_musician(request):
  musician_lists = MusicianModel.objects.all()
  return render(request, 'musician/list_musician.html', { 'data' : musician_lists})