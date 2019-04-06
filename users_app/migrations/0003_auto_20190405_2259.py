# Generated by Django 2.2 on 2019-04-06 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups_app', '0003_auto_20190405_2259'),
        ('users_app', '0002_userapp_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userapp',
            name='group',
        ),
        migrations.AddField(
            model_name='userapp',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='groups_app.GroupApp'),
            preserve_default=False,
        ),
    ]