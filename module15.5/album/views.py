from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm
from .models import AlbumModel

# Create your views here.

# list of album 
def list_album(request):
    data = AlbumModel.objects.all()
    return render(request, 'album/list_album.html', { 'data': data })

# add album 
def add_album(request):
    if request.method == 'POST':
        form =  AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_album')  
    else:
        form = AlbumForm()
        
    return render(request, "album/add_album.html", { 'form' : form})

# edit album 
def edit_album(request, id):
    album = get_object_or_404(AlbumModel, pk=id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('list_album')  
    else:
        form = AlbumForm(instance=album)
    return render(request, 'album/add_album.html', {'form': form})

#delete album  
def delete_album(request, id):
  musician = AlbumModel.objects.get(pk=id) 
  musician.delete()
  return redirect('list_album')