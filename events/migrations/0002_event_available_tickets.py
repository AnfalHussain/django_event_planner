# Generated by Django 2.2.5 on 2019-09-08 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='available_tickets',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]