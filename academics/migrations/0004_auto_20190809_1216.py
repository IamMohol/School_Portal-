# Generated by Django 2.2.2 on 2019-08-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0003_unitregistration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unitregistration',
            options={'verbose_name_plural': 'Unit registration'},
        ),
        migrations.AddField(
            model_name='unitdetail',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
