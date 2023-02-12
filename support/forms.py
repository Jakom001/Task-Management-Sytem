from django import forms
from django.forms import ModelForm

from support.models import Support
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = Support
        fields = ('name', 'extension', 'assigned_to', 'department', 'summary', 'category', 'priority', 'solution', 'status',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "User's name"}),
            'extension': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'i.e 41213'}),
            'category': forms.Select(attrs={'class': 'form-select md3'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'i.e Level 10, Nurses Desk'}),
            'summary': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '4', 'placeholder': 'Describe the issue'}),
            'priority': forms.Select(attrs={'class': 'form-select md3'}),
            'solution': forms.Textarea(
                attrs={'class': 'form-control md3', 'rows': '3'}),
            'status': forms.Select(attrs={'class': 'form-select md3'}),
        }
        assigned_to = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}))

