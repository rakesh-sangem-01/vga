# Generated by Django 5.1.2 on 2024-11-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userapp", "0002_rename_taskname_task_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]
