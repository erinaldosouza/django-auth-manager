# Generated by Django 2.2 on 2019-04-06 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes_app', '0001_initial'),
        ('groups_app', '0004_auto_20190405_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupapp',
            name='route',
        ),
        migrations.AddField(
            model_name='groupapp',
            name='route',
            field=models.ManyToManyField(to='routes_app.RouteApp'),
        ),
    ]
