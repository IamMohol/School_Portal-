# Generated by Django 2.2.2 on 2019-08-14 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0004_auto_20190809_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('avatar', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='unitdetail',
            name='difficulty',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
