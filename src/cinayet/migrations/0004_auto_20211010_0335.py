# Generated by Django 3.1 on 2021-10-10 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinayet', '0003_auto_20211010_0300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cinayet',
            options={'ordering': ['id'], 'verbose_name': 'Cinayət və Hərbi işlər', 'verbose_name_plural': 'Cinayət və Hərbi işləri'},
        ),
        migrations.AlterField(
            model_name='cinayet',
            name='növ',
            field=models.CharField(choices=[('_____', '______'), ('1', '1'), ('1-1', '1-1'), ('7', '7')], default='______', max_length=50),
        ),
        migrations.AlterField(
            model_name='cinayet',
            name='qeyd',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
