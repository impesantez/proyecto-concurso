from django.db import models

class Usage(models.Model):
    device_name = models.CharField(max_length=30, null=False)
    usage = models.DecimalField(null=False, default=1, decimal_places=2, max_digits=6)

    def __str__(self) -> str:
        return f"{self.device_name} - {self.usage}"
