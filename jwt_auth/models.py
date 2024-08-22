from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    professional_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'