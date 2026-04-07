from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('VIEWER', 'Viewer'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='VIEWER'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"