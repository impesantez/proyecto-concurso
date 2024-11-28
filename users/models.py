from django.db import models
import datetime
    
class User(models.Model):
    name = models.CharField(max_length=30, null=False)
    username = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return self.name
    
