# Generated by Django 5.1.1 on 2024-10-10 01:56

import cloudinary.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('title', models.CharField(max_length=100)),
                ('tag_category', models.CharField(choices=[('nature', 'nature'), ('art', 'art'), ('scenery', 'scenary'), ('landscape', 'landscape')], default='nature', max_length=40)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_photos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
