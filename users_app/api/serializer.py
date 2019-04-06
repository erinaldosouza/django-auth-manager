from rest_framework import serializers

from groups_app.api.serializer import GroupAppSerializer
from users_app.models import UserApp


# Create your models here.
class UserAppSerializer(serializers.ModelSerializer):
    group = GroupAppSerializer(many=True, read_only=True)

    class Meta:
        model = UserApp
        fields = ('name', 'last_name', 'login', 'fl_active', 'group')
