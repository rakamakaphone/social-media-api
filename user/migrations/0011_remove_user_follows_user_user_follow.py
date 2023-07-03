# Generated by Django 4.2.2 on 2023-07-03 15:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0010_user_follows_alter_user_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="follows",
        ),
        migrations.AddField(
            model_name="user",
            name="user_follow",
            field=models.ManyToManyField(
                blank=True, related_name="user_followers", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]