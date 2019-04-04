from django.db import models
from routes_app.models import RouteApp


# Create your models here.
class GroupApp(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    fl_active = models.BooleanField(default=False)
    route = models.ManyToManyField(RouteApp)

    def __str__(self):
        return self.name
