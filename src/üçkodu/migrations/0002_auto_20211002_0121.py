# Generated by Django 3.1 on 2021-10-01 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('üçkodu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ückodu',
            name='təqsirləndirilən_şəxs',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
