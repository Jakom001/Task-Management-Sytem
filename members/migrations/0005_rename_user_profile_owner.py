# Generated by Django 4.0.6 on 2022-08-07 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_rename_staff_profile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='owner',
        ),
    ]
