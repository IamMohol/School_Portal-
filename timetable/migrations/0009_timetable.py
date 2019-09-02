# Generated by Django 2.2.2 on 2019-08-17 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0008_auto_20190815_1231'),
        ('timetable', '0008_delete_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('venue', models.CharField(max_length=20)),
                ('clss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Class')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Unit')),
            ],
            options={
                'verbose_name_plural': 'Timetable',
            },
        ),
    ]
