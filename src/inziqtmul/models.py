from django.db import models
from django.db.models.fields import CharField

from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from apps.models import İnstansiyaMahkemesiModel,instansiyaMahkemesihakimiModel,ikinciinstansiyaMahkemesihakimiModel


CHOOSEONE = (
    ('_____', '______'),
    ('2inz', '2inz'),
    ('2iqt', '2iqt'),
    ('2', '2'),
    ('8', '8'),
)

CHOOSETWO = (
    ('_____', '______'),
    ('Qərardad', 'Qərardad'),
    ('Qərar', 'Qərar'),
    ('Etiraz', 'Etiraz'),
    ('Aidiyyət', 'Aidiyyat'),
    ('Müddətin bərpası', 'Müddətin bərpası'),
)

CHOOSETREE = (
    ('_____', '______'),
    ('1 təmin edilmişdir', '1 təmin edilmişdir'),
    ('2 rədd edilmişdir', '2 rədd edilmişdir'),
)

CHOOSEFOUR = (
    ('_____', '______'),
    ('1 - MPM-in 366-cı maddəsi üzrə', '1 - MPM-in 366-cı maddəsi üzrə'),
    ('2 - MPM-in 369-cu maddəsi üzrə', '2 - MPM-in 369-cu maddəsi üzrə'),
    ('3 - MPM-in 370-ci maddəsi üzrə', '3 - MPM-in 370-ci maddəsi üzrə'),
    ('4 - Baxılmadan geri qaytarıldı', '4 - Baxılmadan geri qaytarıldı'),
)

CHOOSEFIVE = (
    ('_____', '______'),
    ('Qərardad', 'Qərardad'),
    ('Qərar', 'Qərar'),
)

CHOOSESIX = (
    ('_____', '______'),
    ('1 - çıxarılmışdır', '1 - çıxarılmışdır'),
    ('2 - çıxarılmamışdır', '2 - çıxarılmamışdır'),
    ('3 - hakim barəsində', '3 - hakim barəsində'),
)

class inziqmulisinNovları(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İşin növünü əlavə et')

    def __str__(self):
        return '%s %s' % (self.name, self.id)

    class Meta: 
        ordering = ['id']
        verbose_name = 'inz iq mul İşin Növü'
        verbose_name_plural = 'inz iq mul İşin Növü'

        

class inziqmulnəticə(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İsim')

    def __str__(self):
        return '%s %s' % (self.name, self.id)

    class Meta: 
        ordering = ['id']
        verbose_name = 'Nəticə'
        verbose_name_plural = 'Nəticə'


class inziqmul(models.Model):
    işin_nömrəsi                        = models.CharField(max_length=50000,blank=True,null=True)
    növ                                 = models.CharField(max_length=500, choices=CHOOSEONE, default='______')
    daxil_olduğu_tarix                  = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    apellyasiya_sikayati_verilmişdir    = models.CharField(max_length=5000, choices=CHOOSETWO, default='______')
    qısa_qeyd                           = models.CharField(max_length=5000,blank=True, null=True)
    instansiyaya_daxil_olmuşdur         = models.DateField(auto_now=False,verbose_name='I instansiyaya daxil olmuşdur', auto_now_add=False,blank=True,null=True)
    instansiya_mahkemesi                = models.ForeignKey(İnstansiyaMahkemesiModel, related_name='inziqmulmahkeme', on_delete=models.CASCADE,blank=False, null=True)
    instansiya_mahkemesi_hakimi         = models.ForeignKey(instansiyaMahkemesihakimiModel, related_name='inziqmulmahkemehakimi', on_delete=models.CASCADE,blank=False, null=True)
    iddiaçı                             = models.CharField(max_length=5000,blank=True, null=True)
    cavabdeh                            = models.CharField(max_length=5000,blank=True, null=True)
    iddianın_mahiyyəti                  = models.CharField(max_length=5000,blank=True, null=True)
    hakimə_edilmiş_etiraz               = models.CharField(max_length=5000, choices=CHOOSETREE, default='______')
    qeyri_mümkün_hesab_edilərək_icraata_xitam_verilmişdir = models.CharField(max_length=50, choices=CHOOSEFOUR, default='______')
    aidiyyət                            = models.BooleanField(blank=True,default=False)
    isin_novu                           = models.ForeignKey(inziqmulisinNovları, related_name='inziqmul_növ', on_delete=models.CASCADE,blank=False, null=True)
    apellyasiya_qaydasında_baxılmışdır  = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    icraat_dayandırılmışdır             = models.BooleanField(blank=True,default=False)
    nəticə                              = models.ForeignKey(inziqmulnəticə, related_name='netica_model', on_delete=models.CASCADE,blank=False, null=True)
    yekun_qərar                         = models.CharField(max_length=5000, choices=CHOOSEFIVE, default='______')
    iki_instansiya_mahkemesi_hakimi     = models.ForeignKey(ikinciinstansiyaMahkemesihakimiModel, related_name='inziqmulmahkemehakimiiki', on_delete=models.CASCADE,blank=False, null=True,verbose_name='2-ci instansiya məhkəməsinin hakimi')
    xüsusi_Qərar                        = models.CharField(max_length=5000, choices=CHOOSESIX, default='______')
    dövlət_rüsumu                       = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    dəftərxanaya_təhvil_verildi         = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    qeyd                                = models.CharField(max_length=5000,blank=True, null=True) 
    yoxlanıldı                                  = models.BooleanField(blank=True,default=False)    

    def __str__(self):
        return '%s %s' % (self.növ, self.id)


    class Meta:
        ordering = ['id']
        verbose_name = 'İNZ İQT MUL'
        verbose_name_plural = 'İNZ İQT MUL '

