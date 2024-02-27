from django.db import models
from django.db.models.fields import CharField

from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from apps.models import İnstansiyaMahkemesiModel,instansiyaMahkemesihakimiModel,ikinciinstansiyaMahkemesihakimiModel



CHOOSEONE = (
    ('_____', '______'),
    ('4', '4'),
    ('4-1', '4-1'),
)

CHOOSETWO = (
    ('_____', '______'),
    ('1 - təmin edilmişdir;', '1 - təmin edilmişdir;'),
    ('2 - rədd edilmişdir;', '2 - rədd edilmişdir;'),
    ('3 - aidiyyəti üzrə göndərilmişdir;', '3 - aidiyyəti üzrə göndərilmişdir;'),
)


CHOOSETREE = (
    ('_____', '______'),
    ('Şikayət', 'Şikayət'),
    ('Protest', 'Protest'),
    ('Şikayət və protest', 'Şikayət və protest'),
)

CHOOSEFOUR = (
    ('_____', '______'),
    ('_____', '______'),
    ('_____', '______'),
    ('_____', '______'),
    ('_____', '______'),
)

class CinayetNovları(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İsim')

    def __str__(self):
        return '%s %s' % (self.name, self.id)

    class Meta: 
        ordering = ['id']
        verbose_name = 'Cinayet Növü'
        verbose_name_plural = 'Cinayet Növları'

class Vəsatətlə_müraciət_edən_orqan(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İsim')

    def __str__(self):
        return '%s %s' % (self.name, self.id)

    class Meta: 
        ordering = ['id']
        verbose_name = 'Vəsatətlə müraciət edən orqan'
        verbose_name_plural = 'Vəsatətlə müraciət edən orqan'

class Vəsatətin_Mahiyyəti(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İsim')

    def __str__(self):
        return '%s %s' % (self.name, self.id)

    class Meta: 
        ordering = ['id']
        verbose_name = 'Vəsatətin Mahiyyəti'
        verbose_name_plural = 'Vəsatətin Mahiyyəti'


class döddkodu(models.Model):    
    işin_nömrəsi                        = models.CharField(max_length=50000,blank=True,null=True)
    növ                                 = models.CharField(max_length=50000, choices=CHOOSEONE, default='______')
    təqsirləndirilən_şəxs               = models.CharField(max_length=50000,blank=True, null=True)
    cinayətin_növü                      = models.ForeignKey(CinayetNovları, verbose_name='Cinayətin növləri', related_name='cinayət_növ', on_delete=models.CASCADE,blank=False, null=True)
    vəsatətlə_müraciət_edən_orqan       = models.ForeignKey(Vəsatətlə_müraciət_edən_orqan, verbose_name='Vəsatətlə müraciət edən orqan', related_name='vəsatətlə_müraciət_edən_orqan_model', on_delete=models.CASCADE,blank=False, null=True) 
    vəsatətin_mahiyyəti                 = models.ForeignKey(Vəsatətin_Mahiyyəti, verbose_name='Vəsatətin Mahiyyəti', related_name='vəsatətin_mahiyyəti_model', on_delete=models.CASCADE,blank=False, null=True) 
    instansiya_mahkemesi_hakimi         = models.ForeignKey(instansiyaMahkemesihakimiModel, related_name='dördkodumahkemehakimi', on_delete=models.CASCADE,blank=False, null=True,verbose_name='1-ci instansiya məhkəməsi hakimi')
    instansiya_məhkəməsinin_qərarının_tarixi    = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    vəsatətin_baxılma_nəticəsi          = models.CharField(max_length=50000, choices=CHOOSETWO, default='______')
    qərarından                          = models.ForeignKey(İnstansiyaMahkemesiModel, related_name='qərarından_model', on_delete=models.CASCADE,blank=False, null=True)
    şikayət_protest                     = models.CharField(max_length=50, choices=CHOOSETREE, default='______')
    apellyasiya_məhkəməsində_baxılmışdır= models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    iki_instansiya_mahkemesi_hakimi     = models.ForeignKey(ikinciinstansiyaMahkemesihakimiModel, related_name='döddmahkemehakimiiki', on_delete=models.CASCADE,blank=False, null=True,verbose_name='2-ci instansiya məhkəməsinin hakimi')
    dəftərxanaya_Verilmişdir            = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    qeyd                                = models.CharField(max_length=50000,blank=True, null=True) 
    yoxlanıldı                                  = models.BooleanField(blank=True,default=False)     

    def __str__(self):
        return '%s %s' % (self.növ, self.id)


    class Meta:
        ordering = ['id']
        verbose_name = '4 kodu'
        verbose_name_plural = '4 kodu'


