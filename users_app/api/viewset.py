from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from users_app.models import UserApp
from users_app.api.serializer import UserAppSerializer


# Create your views here.
class UserAppViewSet(viewsets.ModelViewSet):

    serializer_class = UserAppSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('login', 'password')

    def get_queryset(self):

        """
        API endpoint that allows users to be viewed or edited.
        """
        queryset = UserApp.objects.all().order_by('id')
        queryset = queryset.filter(fl_active=True)

        return queryset
