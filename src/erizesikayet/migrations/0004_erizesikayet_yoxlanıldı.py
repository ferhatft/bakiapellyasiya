# Generated by Django 3.1 on 2021-10-14 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erizesikayet', '0003_auto_20211010_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='erizesikayet',
            name='yoxlanıldı',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
