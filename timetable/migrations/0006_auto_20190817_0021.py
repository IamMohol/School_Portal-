# Generated by Django 2.2.2 on 2019-08-17 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20190817_0020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='end',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='start',
            new_name='start_time',
        ),
    ]
