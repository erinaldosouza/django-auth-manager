from django.contrib import admin

from users_app.forms import UserForm
from .models import UserApp


class UserAppAdmin(admin.ModelAdmin):
    form = UserForm
    search_fields = ('login', 'name', 'last_name')
    list_display = ('login', 'name', 'last_name')
    list_filter = ('login', 'name', 'last_name')


# Register your models here.
admin.site.register(UserApp, UserAppAdmin)
