from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=30, null=False)
    first_login = models.BooleanField(default=True)

    def __str__(self):
        return self.name
