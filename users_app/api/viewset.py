from rest_framework import viewsets
from users_app.api.render import UserAppJsonRenderer
from users_app.models import UserApp
from users_app.api.serializer import UserAppSerializer


# Create your views here.
class UserAppViewSet(viewsets.ModelViewSet):

    renderer_classes = (UserAppJsonRenderer,)
    serializer_class = UserAppSerializer

    def get_queryset(self):

        login = self.kwargs['login']
        obj = UserApp.objects.filter(login=login)
        return obj
