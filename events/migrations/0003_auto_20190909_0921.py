# Generated by Django 2.2.5 on 2019-09-09 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_event_available_tickets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name_of_event',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='available_tickets',
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_tickets', to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
