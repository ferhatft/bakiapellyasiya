# Generated by Django 3.1 on 2021-10-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('üçkodu', '0006_ückodu_yoxlanıldı'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ückodu',
            name='apellyasiya_məhkəməsinin_qərarı_ilə',
            field=models.CharField(choices=[('_____', '______'), ('1 - qərar dəyişdirilmədən saxlanılmışdır', '1 - qərar dəyişdirilmədən saxlanılmışdır'), ('2 - qərar dəyişdirilmişdir', '2 - qərar dəyişdirilmişdir'), ('3 - qərar ləğv edilmiş və icraata xitam verilmişdir', '3 - qərar ləğv edilmiş və icraata xitam verilmişdir'), ('4 - qərar ləğv edilmiş və yenidən baxılması üçün hakimə göndərilmişdir', '4 - qərar ləğv edilmiş və yenidən baxılması üçün hakimə göndərilmişdir'), ('5 - qərar ləğv edilmiş və aidiyyatı üzrə baxılması üçün göndərilmişdir.', '5 - qərar ləğv edilmiş və aidiyyatı üzrə baxılması üçün göndərilmişdir.')], default='______', max_length=50000),
        ),
        migrations.AlterField(
            model_name='ückodu',
            name='hakimin_qərarından',
            field=models.CharField(choices=[('_____', '______'), ('1 - Şikayət verilmişdir', '1 - Şikayət verilmişdir'), ('2 - Protest verilmişdir', '2 - Protest verilmişdir')], default='______', max_length=50000),
        ),
    ]
