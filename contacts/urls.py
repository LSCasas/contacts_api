from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContactViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contacts')

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserRegistrationView.as_view(), name='user-registration'),
]
