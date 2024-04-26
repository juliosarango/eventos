from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):

    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class UpdateForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=150,
        help_text="Required",
        label="Nombres",
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
            },
        ),
    )

    last_name = forms.CharField(
        max_length=150,
        help_text="Required",
        label="Apellidos",
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
            },
        ),
    )

    telefono = forms.CharField(
        max_length=50,
        help_text="Required",
        label="Telefono",
        required=True,
        widget=forms.Select(
            attrs={
                "class": "form-control",
            },
        ),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "telefono")
