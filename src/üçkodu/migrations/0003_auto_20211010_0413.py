# Generated by Django 3.1 on 2021-10-10 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20211010_0317'),
        ('üçkodu', '0002_auto_20211002_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ückodu',
            name='iki_instansiya_mahkemesi_hakimi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ückodumahkemehakimiiki', to='apps.ikinciinstansiyamahkemesihakimimodel', verbose_name='2-ci instansiya məhkəməsinin hakimi'),
        ),
    ]
