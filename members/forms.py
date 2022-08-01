import email

from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your forms here.
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from support.models import Support


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter username"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))


class NewUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
    }), required=True)

    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
    }))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", 'phone_number', "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomEmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email_id = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email_id, is_active=True).exists():
            raise ValidationError("Email invalid!")

        return email


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password"

    }))

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password"

    }))

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password"
    }))

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
