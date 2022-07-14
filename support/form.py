from django.forms import ModelForm
from django import forms
from .models import Support


class UserForm(ModelForm):
    class Meta:
        model = Support
        fields = ('name', 'extension', 'department', 'summary', 'category', 'assigned', 'status')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "User's name"}),
            'extension': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'i.e 41213'}),
            'category': forms.Select(attrs={'class': 'form-control col-md-4'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i.e Level 10, Nurses Desk'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'placeholder': 'Describe the issue'}),
            'assigned': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'status': forms.Select(attrs={'class': 'form-control col-md-4'}),
        }
