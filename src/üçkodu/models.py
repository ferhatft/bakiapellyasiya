from django.db import models
from django.db.models.fields import CharField

from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from apps.models import İnstansiyaMahkemesiModel,instansiyaMahkemesihakimiModel,ikinciinstansiyaMahkemesihakimiModel



CHOOSEONE = (
    ('_____', '______'),
    ('3 ', '3'),
    ('3-1', '3-1'),
)

CHOOSETWO = (
    ('_____', '______'),
    ('1 - Şikayət verilmişdir', '1 - Şikayət verilmişdir'),
    ('2 - Protest verilmişdir', '2 - Protest verilmişdir'),
)


CHOOSETREE = (
    ('_____', '______'),
    ('1 - qərar dəyişdirilmədən saxlanılmışdır', '1 - qərar dəyişdirilmədən saxlanılmışdır'),
    ('2 - qərar dəyişdirilmişdir', '2 - qərar dəyişdirilmişdir'),
    ('3 - qərar ləğv edilmiş və icraata xitam verilmişdir', '3 - qərar ləğv edilmiş və icraata xitam verilmişdir'),
    ('4 - qərar ləğv edilmiş və yenidən baxılması üçün hakimə göndərilmişdir', '4 - qərar ləğv edilmiş və yenidən baxılması üçün hakimə göndərilmişdir'),
    ('5 - qərar ləğv edilmiş və aidiyyatı üzrə baxılması üçün göndərilmişdir.', '5 - qərar ləğv edilmiş və aidiyyatı üzrə baxılması üçün göndərilmişdir.'),
)

CHOOSEFOUR = (
    ('_____', '______'),
    ('inzibati cərimə;', 'inzibati cərimə;'),
    ('ix-nın törədilməsində alət və ya ix-nın bilavasitə obyekti olmuş predmetin ödənişlə alınması;', 'ix-nın törədilməsində alət və ya ix-nın bilavasitə obyekti olmuş predmetin ödənişlə alınması;'),
    ('xüsusi hüququnun məhdudlaşdırılması;', 'xüsusi hüququnun məhdudlaşdırılması;'),
    ('AR-nın hüdudlarından kənara inzibati qaydada çıxartma;', 'AR-nın hüdudlarından kənara inzibati qaydada çıxartma;'),
    ('inzibati həbs.', 'inzibati həbs.'),
    ('İşin icraatına xitam verildi', 'İşin icraatına xitam verildi'),
    ('ix-nın törədilməsində alət və ya ix-nın bilavasitə obyekti olmuş predmetin müsadirəsi', 'ix-nın törədilməsində alət və ya ix-nın bilavasitə obyekti olmuş predmetin müsadirəsi'),
)


class ückodu(models.Model):
    işin_nömrəsi                        = models.CharField(max_length=50000,blank=True,null=True)
    növ                                 = models.CharField(max_length=5000, choices=CHOOSEONE, default='______')
    dahil_olmuşdur                      = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True,verbose_name='Daxil olma tarixi')
    instansiya_mahkemesi                = models.ForeignKey(İnstansiyaMahkemesiModel, related_name='ückodumahkeme', on_delete=models.CASCADE,blank=False, null=True,verbose_name='1-ci instansiya məhkəməsi')
    instansiya_mahkemesi_hakimi         = models.ForeignKey(instansiyaMahkemesihakimiModel, related_name='ückodumahkemehakimi', on_delete=models.CASCADE,blank=False, null=True,verbose_name='1-ci instansiya məhkəməsi hakimi')
    instansiya_məhkəməsinin_qərarının_tarixi    = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    təqsirləndirilən_şəxs               = models.CharField(max_length=50000,blank=True,null=True)
    məsuliyyətə_cəlb_olunmuş_şəxs       = models.CharField(max_length=50000,blank=True,null=True)
    təqsirli_bilindiyi_maddə            = models.CharField(max_length=50000,blank=True,null=True)
    qərarın_baxılma_nəticəsi            = models.CharField(max_length=50000, choices=CHOOSEFOUR, default='______')
    hakimin_qərarından                  = models.CharField(max_length=50000, choices=CHOOSETWO, default='______')
    apellyasiya_məhkəməsinin_qərarı_ilə = models.CharField(max_length=50000, choices=CHOOSETREE, default='______')
    iki_instansiya_mahkemesi_hakimi     = models.ForeignKey(ikinciinstansiyaMahkemesihakimiModel, related_name='ückodumahkemehakimiiki', on_delete=models.CASCADE,blank=False, null=True,verbose_name='Apellyasiya məhkəməsinin hakimi')
    dftərxanaya_verilmişdir             = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    qeyd                                = models.CharField(max_length=50000,blank=True, null=True) 
    yoxlanıldı                                  = models.BooleanField(blank=True,default=False)     


    def __str__(self):
        return '%s %s' % (self.növ, self.id)


    class Meta:
        ordering = ['id']
        verbose_name = 'Üç kodu'
        verbose_name_plural = 'Üç kodu'


