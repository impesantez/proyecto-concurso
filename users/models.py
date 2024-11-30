from django.contrib.auth.hashers import models, make_password
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    name = models.CharField(max_length=30, null=False)
    username = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=False)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    name = models.CharField(max_length=30, null=False)

    
