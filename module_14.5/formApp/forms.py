from django import forms
from .models import Employee


class ContactForm(forms.Form):
    name = forms.CharField(label="Full Name : ", help_text="Total length must be within 70 characters", required=False, error_messages={'required': 'Please enter your name.'},widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class 2', 'placeholder' : 'Enter your name'},))
    email = forms.EmailField(label = "User Email")
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    age = forms.CharField()
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    appointment = forms.CharField()
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL)
    file=forms.FileField()


#student form 

class StudentForm(forms.Form):
    name = forms.CharField(initial= "Your Name ")


# Employee form 


class EmployeeForm(forms.ModelForm):  # Use ModelForm instead of Form
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'name': 'Employee Name',
            'empId': "Employee Id"
        }
        widgets = {
            'name': forms.TextInput(),
        }
        help_texts = {
            'name': "Write your full name"
        }
        
        error_messages = {
            'name': {'required': 'Your name is required'}
        }
