# Generated by Django 2.2.5 on 2019-09-10 11:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190910_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='follow',
            field=models.ManyToManyField(related_name='follow_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
