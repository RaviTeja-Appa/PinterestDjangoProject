# Generated by Django 3.2.13 on 2024-03-01 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PostsByUser', '0002_pin_creation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pin_creation',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='pin_creation',
            name='board',
        ),
        migrations.RemoveField(
            model_name='pin_creation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='pin_creation',
            name='image_Post',
        ),
        migrations.RemoveField(
            model_name='pin_creation',
            name='tagged_topics',
        ),
        migrations.RemoveField(
            model_name='pin_creation',
            name='user',
        ),
    ]
