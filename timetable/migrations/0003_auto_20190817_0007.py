# Generated by Django 2.2.2 on 2019-08-17 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20190816_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='start_time',
            field=models.DateTimeField(verbose_name='%Y-%m-%d %H:%M'),
        ),
    ]
