# Generated by Django 2.2.2 on 2019-07-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20190718_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='time_posted',
        ),
        migrations.AlterField(
            model_name='notifications',
            name='date_posted',
            field=models.DateTimeField(),
        ),
    ]
