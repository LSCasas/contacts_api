from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """MContact model related to a user"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)

    def __str__(self):
        """ Returns a string representation of the object.

        Returns:
            _str: The string representation of the object (name and email).
        """
        return f"{self.name} ({self.email})"
