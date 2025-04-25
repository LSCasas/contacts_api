from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    """Serializador de contactos"""

    class Meta:
        model = models.Contact
        fields = ['id', 'name', 'email', 'phone', 'address']
