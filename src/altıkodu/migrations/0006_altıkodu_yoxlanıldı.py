# Generated by Django 3.1 on 2021-10-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('altıkodu', '0005_auto_20211014_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='altıkodu',
            name='yoxlanıldı',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
