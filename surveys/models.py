from django.db import models

class ElectricitySurvey(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    electricity_usage = models.PositiveIntegerField(help_text="Consumo mensual estimado en kWh")
    num_appliances = models.PositiveIntegerField(help_text="Número de electrodomésticos en tu hogar")
    renewable_usage = models.BooleanField(default=False, help_text="¿Usas fuentes de energía renovables?")
    
    def __str__(self):
        return f"{self.name} - {self.electricity_usage} kWh"