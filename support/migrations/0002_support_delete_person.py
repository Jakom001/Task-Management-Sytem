# Generated by Django 4.0.6 on 2022-07-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('extention', models.IntegerField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('Assigned', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'New'), (2, 'Completed'), (3, 'Archived')])),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]