from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from . import models

class ConductorForm(forms.ModelForm):
	class Meta:
		model = models.Conductor
		fields = "__all__"


class VehiculoForm(forms.ModelForm):
	class Meta:
		model = models.Vehiculo
		fields = "__all__"


class ViajeForm(forms.ModelForm):
	class Meta:
		model = models.Viaje
		fields = "__all__"


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = ["email","username", "password1", "password2"]
        widgets = {
            "email": forms.EmailInput(),
			"username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"})
        }

