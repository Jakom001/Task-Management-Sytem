# Generated by Django 4.0.6 on 2022-08-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_phone_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='Profile_images'),
        ),
    ]
