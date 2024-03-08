# Generated by Django 3.1.7 on 2024-03-08 06:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_blog_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blog_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
