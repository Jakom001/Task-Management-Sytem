from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.
from django.forms import ModelForm

from support.models import Support


class NewUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter username"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter First Name"
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter Last Name"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Enter email address"
    }), required=True)

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Enter password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Re-enter password"
    }))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
