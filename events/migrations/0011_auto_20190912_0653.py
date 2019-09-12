# Generated by Django 2.2.5 on 2019-09-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_anotheruserprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_photo',
            new_name='photo',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AnotherUserProfile',
        ),
    ]
