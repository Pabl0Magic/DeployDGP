# Generated by Django 3.2.17 on 2023-11-18 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0002_auto_20231116_1142"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dooropen",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 40, 20, 469270)
            ),
        ),
        migrations.AlterField(
            model_name="lightison",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 40, 20, 468665)
            ),
        ),
        migrations.AlterField(
            model_name="roomco2",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 40, 20, 468096)
            ),
        ),
        migrations.AlterField(
            model_name="roompeople",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 40, 20, 467429)
            ),
        ),
        migrations.AlterField(
            model_name="roomtemperature",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 40, 20, 467727)
            ),
        ),
        migrations.AlterField(
            model_name="ventilatorison",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 40, 20, 468378)
            ),
        ),
        migrations.AlterField(
            model_name="windowopen",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 40, 20, 468985)
            ),
        ),
    ]
