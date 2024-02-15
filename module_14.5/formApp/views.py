from django.shortcuts import render,redirect
from .forms import ContactForm, StudentForm, EmployeeForm
import os
from . import models

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = {}
        data['email'] = request.POST.get('email') 
        data['username'] = request.POST.get('username')
        return render(request, 'HtmlForm.html', {"data": data})
    else:
        return render(request, 'HtmlForm.html')

# Django Form 
def djangoForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            upload_dir = './formApp/uploads/'
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            with open(os.path.join(upload_dir, file.name), 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = ContactForm()
        
    return render(request, 'django_form.html', {'form': form})

# Student Form 
def studentForm(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data);
            
    else:
        form = StudentForm()
        
    return render(request,'student_form.html', { 'form' : form})


# employee 
def employee_form_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-page')
    else:
        form = EmployeeForm()
    return render(request, "employee_form.html", {'form': form})