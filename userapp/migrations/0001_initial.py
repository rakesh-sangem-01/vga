# Generated by Django 5.1.2 on 2024-11-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("taskname", models.CharField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
