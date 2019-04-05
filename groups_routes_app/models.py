from django.db import models


# Create your models here.
from groups_app.models import GroupApp
from routes_app.models import RouteApp


class GroupRouteApp(models.Model):

    group = models.ForeignKey(GroupApp, blank=False, on_delete=models.DO_NOTHING)
    route = models.ForeignKey(RouteApp, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.group.name + ": " + self.route.description + " - " + self.route.link
