# Generated by Django 3.2.17 on 2023-11-16 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='doorNumber',
        ),
        migrations.RemoveField(
            model_name='room',
            name='lightsBool',
        ),
        migrations.RemoveField(
            model_name='room',
            name='ventilatorBool',
        ),
        migrations.RemoveField(
            model_name='room',
            name='windowNumber',
        ),
    ]