# Generated by Django 5.1.1 on 2024-09-11 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='length_of_stay',
        ),
        migrations.AddField(
            model_name='reservation',
            name='arrival_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='departure_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
