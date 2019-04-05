from django.db import models
from groups_app.models import GroupApp
from users_app.models import UserApp


# Create your models here.
class UserGroupApp(models.Model):

    group = models.ForeignKey(GroupApp, blank=False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(UserApp, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.group.name + " - " + self.user.name
