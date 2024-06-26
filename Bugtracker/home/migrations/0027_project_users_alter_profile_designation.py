# Generated by Django 5.0.3 on 2024-04-14 22:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0026_profile"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="users",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="profile",
            name="Designation",
            field=models.CharField(default="Client", max_length=50),
        ),
    ]
