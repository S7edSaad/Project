# Generated by Django 5.0.3 on 2024-04-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0019_remove_bug_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="createuser",
            name="designation",
            field=models.CharField(default="User", max_length=50),
            preserve_default=False,
        ),
    ]