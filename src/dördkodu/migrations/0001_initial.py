# Generated by Django 3.1 on 2021-10-01 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0002_auto_20210925_0303'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinayetNovları',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
            ],
            options={
                'verbose_name': 'Cinayet Növü',
                'verbose_name_plural': 'Cinayet Növları',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Vəsatətin_Mahiyyəti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
            ],
            options={
                'verbose_name': 'Vəsatətin Mahiyyəti',
                'verbose_name_plural': 'Vəsatətin Mahiyyəti',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Vəsatətlə_müraciət_edən_orqan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
            ],
            options={
                'verbose_name': 'Vəsatətlə müraciət edən orqan',
                'verbose_name_plural': 'Vəsatətlə müraciət edən orqan',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='döddkodu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('işin_nömrəsi', models.CharField(blank=True, max_length=50000, null=True)),
                ('növ', models.CharField(choices=[('_____', '______'), ('4', '4'), ('4-1', '4-1')], default='______', max_length=50000)),
                ('təqsirləndirilən_şəxs', models.CharField(blank=True, max_length=50000, null=True)),
                ('instansiya_məhkəməsinin_qərarının_tarixi', models.DateField(blank=True, null=True)),
                ('vəsatətin_baxılma_nəticəsi', models.CharField(choices=[('_____', '______'), ('01 - təmin edilmişdir;', '01 - təmin edilmişdir;'), ('02 - rədd edilmişdir;', '02 - rədd edilmişdir;'), ('03 - aidiyyəti üzrə göndərilmişdir;', '03 - aidiyyəti üzrə göndərilmişdir;')], default='______', max_length=50000)),
                ('şikayət_protest', models.CharField(choices=[('_____', '______'), ('Şikayət', 'Şikayət'), ('Protest', 'Protest'), ('Şikayət və protest', 'Şikayət və protest')], default='______', max_length=50)),
                ('apellyasiya_məhkəməsində_baxılmışdır', models.DateField(blank=True, null=True)),
                ('dəftərxanaya_Verilmişdir', models.DateField(blank=True, null=True)),
                ('qeyd', models.CharField(blank=True, max_length=50000, null=True)),
                ('cinayətin_növü', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cinayət_növ', to='dördkodu.cinayetnovları', verbose_name='Cinayətin növləri')),
                ('iki_instansiya_mahkemesi_hakimi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='döddmahkemehakimiiki', to='apps.ikinciinstansiyamahkemesihakimimodel')),
                ('instansiya_mahkemesi_hakimi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dördkodumahkemehakimi', to='apps.instansiyamahkemesihakimimodel')),
                ('qərarından', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qərarından_model', to='apps.instansiyamahkemesihakimimodel')),
                ('vəsatətin_mahiyyəti', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vəsatətin_mahiyyəti_model', to='dördkodu.vəsatətin_mahiyyəti', verbose_name='Vəsatətin Mahiyyəti')),
                ('vəsatətlə_müraciət_edən_orqan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vəsatətlə_müraciət_edən_orqan_model', to='dördkodu.vəsatətlə_müraciət_edən_orqan', verbose_name='Vəsatətlə müraciət edən orqan')),
            ],
            options={
                'verbose_name': 'Dörd kodu',
                'verbose_name_plural': 'Dörd kodu',
                'ordering': ['id'],
            },
        ),
    ]
