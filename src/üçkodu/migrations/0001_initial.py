# Generated by Django 3.1 on 2021-09-30 23:30

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
            name='ückodu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('işin_nömrəsi', models.CharField(blank=True, max_length=50000, null=True)),
                ('növ', models.CharField(choices=[('_____', '______'), ('xəbrədarlıq;', 'xəbrədarlıq;'), ('inzibati cərimə;', 'inzibati cərimə;'), ('ix-nın törədilməsində alət və ya ix-nın bilavasitə obyekti olmuş predmetin ödənişlə alınması;', 'ix-nın törədilməsində alət və ya ix-nın bilavasitə obyekti olmuş predmetin ödənişlə alınması;'), ('xüsusi hüququnun məhdudlaşdırılması;', 'xüsusi hüququnun məhdudlaşdırılması;'), ('AR-nın hüdudlarından kənara inzibati qaydada çıxartma;', 'AR-nın hüdudlarından kənara inzibati qaydada çıxartma;'), ('inzibati həbs.', 'inzibati həbs.'), ('İşin icraatına xitam verildi', 'İşin icraatına xitam verildi')], default='______', max_length=5000)),
                ('dahil_olmuşdur', models.DateField(blank=True, null=True)),
                ('instansiya_məhkəməsinin_qərarının_tarixi', models.DateField(blank=True, null=True)),
                ('təqsirləndirilən_şəxs', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('məsuliyyətə_cəlb_olunmuş_şəxs', models.CharField(blank=True, max_length=50000, null=True)),
                ('təqsirli_bilindiyi_maddə', models.CharField(blank=True, max_length=50000, null=True)),
                ('qərarın_baxılma_nəticəsi', models.CharField(choices=[('_____', '______'), ('xəbrədarlıq;', 'xəbrədarlıq;'), ('inzibati cərimə;', 'inzibati cərimə;'), ('ix-nın törədilməsində alət və ya ix-nın bilavasitə obyekti olmuş predmetin ödənişlə alınması;', 'ix-nın törədilməsində alət və ya ix-nın bilavasitə obyekti olmuş predmetin ödənişlə alınması;'), ('xüsusi hüququnun məhdudlaşdırılması;', 'xüsusi hüququnun məhdudlaşdırılması;'), ('AR-nın hüdudlarından kənara inzibati qaydada çıxartma;', 'AR-nın hüdudlarından kənara inzibati qaydada çıxartma;'), ('inzibati həbs.', 'inzibati həbs.'), ('İşin icraatına xitam verildi', 'İşin icraatına xitam verildi')], default='______', max_length=50000)),
                ('hakimin_qərarından', models.CharField(choices=[('_____', '______'), ('01 - Şikayət verilmişdir', '01 - Şikayət verilmişdir'), ('02 - Protest verilmişdir', '02 - Protest verilmişdir')], default='______', max_length=50000)),
                ('apellyasiya_məhkəməsinin_qərarı_ilə', models.CharField(choices=[('_____', '______'), ('01 - qərar dəyişdirilmədən saxlanılmışdır', '01 - qərar dəyişdirilmədən saxlanılmışdır'), ('02 - qərar dəyişdirilmişdir', '02 - qərar dəyişdirilmişdir'), ('03 - qərar ləğv edilmiş və icraata xitam verilmişdir', '03 - qərar ləğv edilmiş və icraata xitam verilmişdir'), ('04 - qərar ləğv edilmiş və yenidən baxılması üçün hakimə göndərilmişdir', '04 - qərar ləğv edilmiş və yenidən baxılması üçün hakimə göndərilmişdir'), ('05 - qərar ləğv edilmiş və aidiyyatı üzrə baxılması üçün göndərilmişdir.', '05 - qərar ləğv edilmiş və aidiyyatı üzrə baxılması üçün göndərilmişdir.')], default='______', max_length=50000)),
                ('dftərxanaya_verilmişdir', models.DateField(blank=True, null=True)),
                ('qeyd', models.CharField(blank=True, max_length=50000, null=True)),
                ('iki_instansiya_mahkemesi_hakimi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ückodumahkemehakimiiki', to='apps.ikinciinstansiyamahkemesihakimimodel')),
                ('instansiya_mahkemesi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ückodumahkeme', to='apps.i̇nstansiyamahkemesimodel')),
                ('instansiya_mahkemesi_hakimi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ückodumahkemehakimi', to='apps.instansiyamahkemesihakimimodel')),
            ],
            options={
                'verbose_name': 'Üç kodu',
                'verbose_name_plural': 'Üç kodu',
                'ordering': ['id'],
            },
        ),
    ]
