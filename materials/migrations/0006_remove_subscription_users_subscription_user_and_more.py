# Generated by Django 5.0.6 on 2024-06-14 18:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0005_subscription"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="users",
        ),
        migrations.AddField(
            model_name="subscription",
            name="user",
            field=models.ForeignKey(
                default=13,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="subscription",
            name="course",
            field=models.ForeignKey(
                default=5,
                on_delete=django.db.models.deletion.CASCADE,
                to="materials.course",
            ),
            preserve_default=False,
        ),
    ]
