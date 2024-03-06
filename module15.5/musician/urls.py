from django.urls import path
from . import views


urlpatterns = [
    path('addMusician/', views.addMusician,  name='addMusician' ), 
    path('view_musician_list', views.list_musician, name='view_musician_list'),
    path('editMusician/<int:id>', views.editMusician, name='editMusician'), 
    path('deleteMusician/<int:id>', views.deleteMusician, name='deleteMusician')
]
