# Generated by Django 3.1 on 2021-10-01 20:58

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apps', '0002_auto_20210925_0303'),
    ]

    operations = [
        migrations.CreateModel(
            name='inziqmulisinNovları',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
            ],
            options={
                'verbose_name': 'inz iq mul İşin Növü',
                'verbose_name_plural': 'inz iq mul İşin Növü',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='inziqmulnəticə',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='İsim')),
            ],
            options={
                'verbose_name': 'Nəticə',
                'verbose_name_plural': 'Nəticə',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='inziqmul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('işin_nömrəsi', models.CharField(blank=True, max_length=50000, null=True)),
                ('növ', models.CharField(choices=[('_____', '______'), ('2inz', '2inz'), ('2iqt', '2iqt'), ('2', '2'), ('8', '8')], default='______', max_length=500)),
                ('daxil_olduğu_tarix', models.DateField(blank=True, null=True)),
                ('apellyasiya_sikayati_verilmişdir', models.CharField(choices=[('_____', '______'), ('Qərardad', 'Qərardad'), ('Qərar', 'Qərar'), ('Etiraz', 'Etiraz'), ('Aidiyyət', 'Aidiyyat'), ('Müddətin bərpası', 'Müddətin bərpası')], default='______', max_length=5000)),
                ('qısa_qeyd', models.CharField(blank=True, max_length=5000, null=True)),
                ('instansiyaya_daxil_olmuşdur', models.DateField(blank=True, null=True, verbose_name='I instansiyaya daxil olmuşdur')),
                ('iddiaçı', models.CharField(blank=True, max_length=5000, null=True)),
                ('cavabdeh', models.CharField(blank=True, max_length=5000, null=True)),
                ('iddianın_mahiyyəti', models.CharField(blank=True, max_length=5000, null=True)),
                ('hakimə_edilmiş_etiraz', models.CharField(choices=[('_____', '______'), ('01 təmin edilmişdir', '01 təmin edilmişdir'), ('02 rədd edilmişdir', '02 rədd edilmişdir')], default='______', max_length=5000)),
                ('qeyri_mümkün_hesab_edilərək_icraata_xitam_verilmişdir', models.CharField(choices=[('_____', '______'), ('01 - MPM-in 366-cı maddəsi üzrə', '01 - MPM-in 366-cı maddəsi üzrə'), ('02 - MPM-in 369-cu maddəsi üzrə', '02 - MPM-in 369-cu maddəsi üzrə'), ('03 - MPM-in 370-ci maddəsi üzrə', '03 - MPM-in 370-ci maddəsi üzrə')], default='______', max_length=50)),
                ('aidiyyət', models.BooleanField(blank=True, default=False)),
                ('apellyasiya_qaydasında_baxılmışdır', models.DateField(blank=True, null=True)),
                ('icraat_dayandırılmışdır', models.BooleanField(blank=True, default=False)),
                ('yekun_qərar', models.CharField(choices=[('_____', '______'), ('Qərardad', 'Qərardad'), ('Qərar', 'Qərar')], default='______', max_length=5000)),
                ('xüsusi_Qərar', models.CharField(choices=[('_____', '______'), ('01 - çıxarılmışdır', '01 - çıxarılmışdır'), ('02 - çıxarılmamışdır', '02 - çıxarılmamışdır'), ('03 - hakim barəsində', '03 - hakim barəsində')], default='______', max_length=5000)),
                ('dövlət_rüsumu', models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True)),
                ('dəftərxanaya_təhvil_verildi', models.DateField(blank=True, null=True)),
                ('qeyd', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('iki_instansiya_mahkemesi_hakimi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inziqmulmahkemehakimiiki', to='apps.ikinciinstansiyamahkemesihakimimodel')),
                ('instansiya_mahkemesi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inziqmulmahkeme', to='apps.i̇nstansiyamahkemesimodel')),
                ('instansiya_mahkemesi_hakimi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inziqmulmahkemehakimi', to='apps.instansiyamahkemesihakimimodel')),
                ('isin_novu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inziqmul_növ', to='inziqtmul.inziqmulisinnovları')),
                ('nəticə', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='netica_model', to='inziqtmul.inziqmulnəticə')),
            ],
            options={
                'verbose_name': 'inz iq mul',
                'verbose_name_plural': 'inz iq mul',
                'ordering': ['id'],
            },
        ),
    ]
