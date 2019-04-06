from rest_framework import serializers

from groups_app.models import GroupApp
from routes_app.api.serializer import RouteAppSerializer


# Create your models here.
from routes_app.models import RouteApp


class GroupAppSerializer(serializers.ModelSerializer):

    route = RouteAppSerializer(many=True, read_only=True)

    class Meta:
        model = GroupApp
        fields = ('name', 'description', 'fl_active', 'route')

