# Generated by Django 4.1.6 on 2023-11-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0019_door_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='day',
            field=models.IntegerField(default=-1),
        ),
    ]
