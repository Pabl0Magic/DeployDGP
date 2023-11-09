# Generated by Django 3.2.17 on 2023-11-06 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20231030_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='doorNumber',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='lightsBool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='ventilatorBool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='windowNumber',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='dooropen',
            name='door',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.door'),
        ),
        migrations.AlterField(
            model_name='light',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.room'),
        ),
        migrations.AlterField(
            model_name='lightison',
            name='light',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.light'),
        ),
        migrations.AlterField(
            model_name='roomco2',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.room'),
        ),
        migrations.AlterField(
            model_name='roompeople',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.room'),
        ),
        migrations.AlterField(
            model_name='roomtemperature',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.room'),
        ),
        migrations.AlterField(
            model_name='ventilator',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.room'),
        ),
        migrations.AlterField(
            model_name='ventilatorison',
            name='ventilator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.ventilator'),
        ),
        migrations.AlterField(
            model_name='window',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.room'),
        ),
        migrations.AlterField(
            model_name='windowopen',
            name='window',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.window'),
        ),
    ]