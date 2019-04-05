from django.db import models


# Create your models here.
class UserApp(models.Model):

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    login = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

    fl_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " " + self.last_name
