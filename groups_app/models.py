from django.db import models


# Create your models here.
class GroupApp(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    fl_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " - " + self.description
