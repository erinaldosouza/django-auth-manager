# Generated by Django 2.2 on 2019-04-06 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes_app', '0001_initial'),
        ('groups_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupapp',
            name='group',
            field=models.ManyToManyField(to='routes_app.RouteApp'),
        ),
    ]
