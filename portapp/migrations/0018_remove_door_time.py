# Generated by Django 4.1.6 on 2023-11-21 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0017_remove_door_d2_remove_doorfail_d2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='door',
            name='time',
        ),
    ]
