from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """Modelo de contacto relacionado a un usuario"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
