from rest_framework import viewsets, permissions, status
from . import models, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer


class ContactViewSet(viewsets.ModelViewSet):
    """CRUD of authenticated user contacts"""
    serializer_class = serializers.ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

# CREATE CONTACT
    def perform_create(self, serializer):
        """Creates an contact with the current user as the owner.

        Args:
            serializer (Serializer): Validated serializer.
        """
        serializer.save(user=self.request.user)

# GET CONTACTS
    def get_queryset(self):
        """
        Returns contacts belonging to the current user.
        """
        return models.Contact.objects.filter(user=self.request.user)

# EDIT CONTACT
    def perform_update(self, serializer):
        """Updates an object with the current user as the owner.

        Args:
            serializer (Serializer): Validated serializer.
        """
        serializer.save(user=self.request.user)

# DELETE CONTACT
    def perform_destroy(self, instance):
        """Deletes the given object instance.

        Args:
            instance (Model): The object to delete.
        """
        instance.delete()

# CREATE A NEW USER


class UserRegistrationView(APIView):
    """View to register new users"""
    permission_classes = []

    def post(self, request):
        """Handles user registration via POST request.

        Args:
            request (Request): The incoming HTTP request with user data.

        Returns:
            Response: Success response with user info or error details.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
