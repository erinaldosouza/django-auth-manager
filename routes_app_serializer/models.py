from django.db import models

# Create your models here.
from rest_framework import serializers

from routes_app.models import RouteApp


class RouteAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteApp
        fields = ('app_name', 'link', 'fl_active', 'description')
