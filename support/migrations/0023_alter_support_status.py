# Generated by Django 4.0.6 on 2022-07-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0022_alter_support_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='status',
            field=models.CharField(choices=[(1, 'New'), (2, 'Completed'), (3, 'Review')], default='New', max_length=120),
        ),
    ]