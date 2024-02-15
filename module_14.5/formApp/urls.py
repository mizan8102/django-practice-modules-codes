from django.urls import path
from .import views
urlpatterns =[
    path('htmlForm/',  views.home, name="htmlForm" ),
    path('djangoForm/',  views.djangoForm, name="djangoForm" ),
    path('employeeForm/',views.employee_form_view, name="employeeForm")
]