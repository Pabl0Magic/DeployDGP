# Generated by Django 3.2.17 on 2023-11-18 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0003_auto_20231118_1140"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dooropen",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 43, 4, 987173, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="lightison",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 43, 4, 986469, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="roomco2",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 43, 4, 985855, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="roompeople",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 43, 4, 985030, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="roomtemperature",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 43, 4, 985445, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="ventilatorison",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 43, 4, 986140, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="windowopen",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 18, 11, 43, 4, 986854, tzinfo=utc)
            ),
        ),
    ]