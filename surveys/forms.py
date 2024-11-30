from django import forms
from .models import ElectricitySurvey

class ElectricitySurveyForm(forms.ModelForm):
    class Meta:
        model = ElectricitySurvey
        fields = ['name', 'email', 'electricity_usage', 'num_appliances', 'renewable_usage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'electricity_usage': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_appliances': forms.NumberInput(attrs={'class': 'form-control'}),
            'renewable_usage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
