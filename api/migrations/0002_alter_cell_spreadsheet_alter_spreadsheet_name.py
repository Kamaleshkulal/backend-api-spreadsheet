# Generated by Django 5.1.6 on 2025-02-27 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cell",
            name="spreadsheet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cells",
                to="api.spreadsheet",
            ),
        ),
        migrations.AlterField(
            model_name="spreadsheet",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
