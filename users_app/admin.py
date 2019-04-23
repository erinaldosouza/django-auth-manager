from django.contrib import admin
from .models import UserApp


class UserAppAdmin(admin.ModelAdmin):
    list_display = ('login', 'name', 'last_name')
    list_filter = ('login', 'name', 'last_name')
    search_fields = ('login', 'name', 'last_name')


# Register your models here.
admin.site.register(UserApp, UserAppAdmin)
