# Generated by Django 3.1 on 2021-10-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('altıkodu', '0006_altıkodu_yoxlanıldı'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altıkodu',
            name='apellyasiya_məhkəməsi',
            field=models.CharField(choices=[('_____', '______'), ('1 - qərarı dəyişdirmədən saxlamışdır', '1 - qərarı dəyişdirmədən saxlamışdır'), ('2 - qərarı ləğv etmişdir', '2 - qərarı ləğv etmişdir')], default='______', max_length=50000),
        ),
        migrations.AlterField(
            model_name='altıkodu',
            name='apellyasiya_qayadısnda',
            field=models.CharField(choices=[('_____', '______'), ('1 - şikayət verilmişdir', '1 - şikayət verilmişdir'), ('2 - protest verilmişdir', '2 - protest verilmişdir')], default='______', max_length=50000),
        ),
        migrations.AlterField(
            model_name='altıkodu',
            name='şikayət_verilmişdir',
            field=models.CharField(choices=[('_____', '______'), ('1 - təhqiqatçının (onun səlahiyyətlərini həyata keçirən şəxsin)', '1 - təhqiqatçının (onun səlahiyyətlərini həyata keçirən şəxsin)'), ('2 - tutulmanı və ya tutulan şəxsin həbsdə saxlanılma yerlərində saxlanılmasını həyata keçirən şəxsin', '2 - tutulmanı və ya tutulan şəxsin həbsdə saxlanılma yerlərində saxlanılmasını həyata keçirən şəxsin'), ('3 - əməliyyat-axtarış fəaliyyətini həyata keçirən şəxsin', '3 - əməliyyat-axtarış fəaliyyətini həyata keçirən şəxsin'), ('5 - ibtidai araşdırmaya prosessual rəhbərliyi həyata keçirən prokurorun', '5 - ibtidai araşdırmaya prosessual rəhbərliyi həyata keçirən prokurorun')], default='______', max_length=50000),
        ),
        migrations.AlterField(
            model_name='altıkodu',
            name='şikayətə_baxılmanın_nəticəsi',
            field=models.CharField(choices=[('_____', '______'), ('1 - təmin olunmuşdur', '1 - təmin olunmuşdur'), ('2 - rədd olunmuşdur', '2 - rədd olunmuşdur'), ('3 - aidiyyəti üzrə göndərilmişdir', '3 - aidiyyəti üzrə göndərilmişdir')], default='______', max_length=50000),
        ),
    ]
