from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from users_app.models import UserApp
from users_app.api.serializer import UserAppSerializer


class UserAppViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserApp.objects.all().order_by('id')
    serializer_class = UserAppSerializer

