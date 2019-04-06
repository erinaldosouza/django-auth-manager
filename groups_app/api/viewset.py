from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from groups_app.models import GroupApp
from  groups_app.api.serializer import GroupAppSerializer


class GroupAppViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GroupApp.objects.all().order_by('id')
    serializer_class = GroupAppSerializer
