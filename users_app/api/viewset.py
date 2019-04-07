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
        TODO request without the specified headers will throw exception. It's necessary to figure out how to get customs response with django rest.
        """
        name = self.request.META['HTTP_USER_APP_NAME']
        password = self.request.META['HTTP_USER_APP_PASSWORD']

        queryset = UserApp.objects.all().order_by('id')
        queryset = queryset.filter(fl_active=True, login=name, password=password)

        return queryset



