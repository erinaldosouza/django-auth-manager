from rest_framework import viewsets

from groups_app.models import GroupApp
from groups_app.api.serializer import GroupAppSerializer


# Create your views here.
class GroupAppViewSet(viewsets.ModelViewSet):

    serializer_class = GroupAppSerializer

    def get_queryset(self):

        """
        API endpoint that allows groups to be viewed or edited.
        """
        queryset = GroupApp.objects.all().order_by('id')
        queryset = queryset.filter(fl_active=True)

        return queryset
