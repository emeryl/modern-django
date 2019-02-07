from django.contrib.auth import get_user_model

from rest_framework import viewsets

from project.api.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint allowing viewing and editing of Users."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
