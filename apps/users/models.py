from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    Role_CHOICES=(
        ('ADMIN','admin'),
        ('MANAGER','manager'),
        ('VIEWER','viewer')
    )
    role=models.CharField(max_length=20,choices=Role_CHOICES,default='VIEWER')

    def __str__(self):
        return self.username