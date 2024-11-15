from django import forms
from .models import Resume, Pyresume
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class resumeForm(forms.ModelForm):
    skills = forms.MultipleChoiceField(
        choices=[
            ('skill1', 'python'),
            ('skill2', 'DSA'),
            ('skill3', 'OOPs'),
            ('skill4', 'javascript'),
            ('skill5', 'HTML, CSS'),
        ],
        widget=forms.CheckboxSelectMultiple,  # This will render checkboxes
        required=False  # Optional, set to True if you want to make it mandatory
    )

    class Meta:
        model = Resume
        fields = ['Name', 'doc', 'year', 'email', 'CGPA', 'skills'] 
        

class pyForm(forms.ModelForm):
    skills = forms.MultipleChoiceField(
        choices=[
            ('skill1', 'python'),
            ('skill2', 'DSA'),
            ('skill3', 'OOPs'),
            ('skill4', 'javascript'),
            ('skill5', 'HTML, CSS'),
        ],
        widget=forms.CheckboxSelectMultiple,  # This will render checkboxes
        required=False  # Optional, set to True if you want to make it mandatory
    )

    class Meta:
        model = Pyresume
        fields = ['Name', 'doc', 'year', 'email', 'CGPA', 'skills'] 



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    