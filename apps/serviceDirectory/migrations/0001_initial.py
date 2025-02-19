# Generated by Django 5.1.1 on 2024-09-10 23:06

import apps.serviceDirectory.models
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=80)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='hotels.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('menu', models.FileField(upload_to=apps.serviceDirectory.models.menu_service_directory)),
                ('header_image', models.ImageField(upload_to=apps.serviceDirectory.models.header_service_directory)),
                ('description', models.TextField()),
                ('availabilities', models.JSONField()),
                ('requirement', models.TextField(blank=True, null=True)),
                ('require_reservation', models.BooleanField(default=False)),
                ('maximum_capacity', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='serviceDirectory.category')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=apps.serviceDirectory.models.header_service_directory)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='serviceDirectory.service')),
            ],
        ),
    ]
