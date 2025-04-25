from rest_framework import viewsets, permissions, status
from . import models, serializers


class ContactViewSet(viewsets.ModelViewSet):
    """CRUD of authenticated user contacts"""
    serializer_class = serializers.ContactSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Creates an contact with the current user as the owner.

        Args:
            serializer (Serializer): Validated serializer.
        """
        serializer.save(user=self.request.user)
