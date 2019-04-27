from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from users_app.api.render import UserAppJsonRenderer
from users_app.models import UserApp
from users_app.api.serializer import UserAppSerializer


# Create your views here.
class UserAppViewSet(viewsets.ModelViewSet):

    renderer_classes = (UserAppJsonRenderer,)
    serializer_class = UserAppSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('login',)

    def get_queryset(self):

        queryset = UserApp.objects.all()
        return queryset
