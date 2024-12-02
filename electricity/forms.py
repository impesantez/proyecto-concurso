from django import forms
from .models import Carbon_footprint, Usage
from django import forms
from .models import Carbon_footprint, Usage

from django import forms
from .models import Carbon_footprint

class AddUsageForm(forms.ModelForm):
    class Meta:
        model = Carbon_footprint
        fields = ['usage', 'daily_hours', 'monthly_times']
        labels = {
            "usage": "Dispositivo",
            "daily_hours": "Horas Diarias",
            "monthly_times": "Veces al Mes"
        }
        widgets = {
            'usage': forms.Select(attrs={'class': 'form-select'}),
            'daily_hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las horas diarias'}),
            'monthly_times': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese las veces al mes'}),
        }

