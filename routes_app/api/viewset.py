from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from routes_app.models import RouteApp
from routes_app.api.serializer import RouteAppSerializer


class RouteAppViewSet(viewsets.ModelViewSet):

    serializer_class = RouteAppSerializer

    def get_queryset(self):
        """
        API endpoint that allows routers to be viewed or edited.
        """
        queryset = RouteApp.objects.all().order_by('id')
        queryset = queryset.filter(fl_active=True)
        return queryset
