from django import forms
from .models import *


class CUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            "name":  "Nombre",
            "username": "Nombre de usuario",
            "email": "Correo electrónico",
            "password": "Contraseña",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'nombre@ejemplo.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }