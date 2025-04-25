from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    """Contact serializer"""

    class Meta:
        model = models.Contact
        fields = ['id', 'name', 'email', 'phone', 'address']


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer to register new users"""
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        """Creates and returns a new user.

        Args:
            validated_data (dict): The validated data for user creation.

        Returns:
            User: The created user instance.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
