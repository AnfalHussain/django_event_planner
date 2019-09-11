# Generated by Django 2.2.5 on 2019-09-10 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_user_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
