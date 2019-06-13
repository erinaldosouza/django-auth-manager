# Generated by Django 2.2 on 2019-06-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routes_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('fl_active', models.BooleanField(default=False)),
                ('route', models.ManyToManyField(to='routes_app.RouteApp')),
            ],
        ),
    ]
