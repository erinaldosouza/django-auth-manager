from django.db import models


# Create your models here.
from routes_app.enums.HttpMethodEnum import HttpMethod


class RouteApp(models.Model):

    app_name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    authorization = models.CharField(max_length=6, choices=[(method.value, method.name) for method in HttpMethod])
    fl_active = models.BooleanField(default=False)

    def __str__(self):
        return self.app_name + " - " + self.link

