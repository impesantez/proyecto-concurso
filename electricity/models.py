from django.db import models
from django.core.exceptions import ValidationError
from decimal import Decimal

class Usage(models.Model):
    device_name = models.CharField(max_length=30, null=False)
    usage_hour = models.DecimalField(null=True, default=None, blank=True, decimal_places=2, max_digits=6)
    usage_per_time = models.DecimalField(null=True, default=None, blank=True, decimal_places=2, max_digits=6)
    
    def __str__(self) -> str:
        return f"{self.device_name}"
        
class Carbon_footprint(models.Model):
    usage = models.ForeignKey("electricity.Usage", on_delete=models.PROTECT)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    daily_hours = models.IntegerField(null=True, default=None, blank=True)
    monthly_times = models.IntegerField(null=True, default = None, blank=True)
    kwh = models.DecimalField(null=False, default=0, decimal_places=2, max_digits=6)
    carbon = models.DecimalField(null=False, default=0, decimal_places=2, max_digits=6)
    
    def calculate_kwh_and_carbon(self):
        if self.daily_hours:
            monthly_hours = self.daily_hours * Decimal('30')
            self.kwh = monthly_hours * self.usage.usage_hour
        elif self.monthly_times:
            self.kwh = self.monthly_times * self.usage.usage_per_time
        else:
            self.kwh = Decimal(0)

        emissions_factor = Decimal('0.2')
        self.carbon = self.kwh * emissions_factor

    def save(self, *args, **kwargs):
        self.calculate_kwh_and_carbon()
        super().save(*args, **kwargs)
        
    def clean(self):
        if self.daily_hours and self.monthly_times:
            raise ValidationError("Specify either daily hours or monthly times, not both.")
        if not self.daily_hours and not self.monthly_times:
            raise ValidationError("Either daily hours or monthly times must be specified.")