from django.db import models
from django.db.models.fields import CharField

from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from apps.models import İnstansiyaMahkemesiModel,instansiyaMahkemesihakimiModel,ikinciinstansiyaMahkemesihakimiModel



CHOOSEONE = (
    ('_____', '______'),
    ('6', '6'),
    ('6-1', '6-1'),
)

CHOOSETWO = (
    ('_____', '______'),
    ('1 - təhqiqatçının (onun səlahiyyətlərini həyata keçirən şəxsin)', '1 - təhqiqatçının (onun səlahiyyətlərini həyata keçirən şəxsin)'),
    ('2 - tutulmanı və ya tutulan şəxsin həbsdə saxlanılma yerlərində saxlanılmasını həyata keçirən şəxsin', '2 - tutulmanı və ya tutulan şəxsin həbsdə saxlanılma yerlərində saxlanılmasını həyata keçirən şəxsin'),
    ('3 - əməliyyat-axtarış fəaliyyətini həyata keçirən şəxsin', '3 - əməliyyat-axtarış fəaliyyətini həyata keçirən şəxsin'),
    ('5 - ibtidai araşdırmaya prosessual rəhbərliyi həyata keçirən prokurorun', '5 - ibtidai araşdırmaya prosessual rəhbərliyi həyata keçirən prokurorun'),
)


CHOOSETREE = (
    ('_____', '______'),
    ('1 - təmin olunmuşdur', '1 - təmin olunmuşdur'),
    ('2 - rədd olunmuşdur', '2 - rədd olunmuşdur'),
    ('3 - aidiyyəti üzrə göndərilmişdir', '3 - aidiyyəti üzrə göndərilmişdir'),
)

CHOOSEFOUR = (
    ('_____', '______'),
    ('1 - şikayət verilmişdir', '1 - şikayət verilmişdir'),
    ('2 - protest verilmişdir', '2 - protest verilmişdir'),
)

CHOOSEFIVE = (
    ('_____', '______'),
    ('1 - qərarı dəyişdirmədən saxlamışdır', '1 - qərarı dəyişdirmədən saxlamışdır'),
    ('2 - qərarı ləğv etmişdir', '2 - qərarı ləğv etmişdir'),
)

class altıkodu(models.Model):
    işin_nömrəsi                        = models.CharField(max_length=50000,blank=True,null=True)
    növ                                 = models.CharField(max_length=50000, choices=CHOOSEONE, default='______')
    daxil_olduğu_tarix                  = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    şikayətlə_müraciət_edən_şəxs        = models.CharField(max_length=50000,blank=True, null=True)
    şikayət_verilmişdir                 = models.CharField(max_length=50000, choices=CHOOSETWO, default='______')
    bir_instansiya_məhkəməsində_baxılmışdır   = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True,verbose_name='I instansiya məhkəməsində baxılmışdır')
    instansiya_mahkemesi                = models.ForeignKey(İnstansiyaMahkemesiModel,verbose_name='1-ci instansiya məhkəməsi',related_name='altıkodumahkeme', on_delete=models.CASCADE,blank=False, null=True)
    instansiya_mahkemesi_hakimi         = models.ForeignKey(instansiyaMahkemesihakimiModel,related_name='altıkodumahkemehakimi', on_delete=models.CASCADE,blank=False, null=True,verbose_name='1-ci instansiya məhkəməsi hakimi')
    şikayətə_baxılmanın_nəticəsi        = models.CharField(max_length=50000, choices=CHOOSETREE, default='______')
    apellyasiya_qayadısnda              = models.CharField(max_length=50000, choices=CHOOSEFOUR, default='______')
    apellyasiya_məhkəməsində_baxılmışdır= models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    iki_instansiya_mahkemesi_hakimi     = models.ForeignKey(ikinciinstansiyaMahkemesihakimiModel,verbose_name='2-ci instansiya məhkəməsinin hakimi' , related_name='altıkodumahkemehakimiiki', on_delete=models.CASCADE,blank=False, null=True)
    apellyasiya_məhkəməsi               = models.CharField(max_length=50000, choices=CHOOSEFIVE, default='______')
    iş_dəftərxanaya_təhvil_verilmişdir= models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    qeyd                                = models.CharField(max_length=50000,blank=True, null=True)  
    yoxlanıldı                                  = models.BooleanField(blank=True,default=False)    

    def __str__(self):
        return '%s %s' % (self.növ, self.id)


    class Meta:
        ordering = ['id']
        verbose_name = '6 kodu'
        verbose_name_plural = '6 kodu'


