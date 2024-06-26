# Generated by Django 3.2.13 on 2024-03-12 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PostsByUser', '0008_following'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PostsByUser.image_posting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_saver', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
