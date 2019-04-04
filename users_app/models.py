from django.db import models

# Create your models here.
from groups_app.models import GroupApp


class UserApp(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    group = models.ManyToManyField(GroupApp)
    fl_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.last_name
