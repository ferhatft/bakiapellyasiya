from django.db import models
from django.db.models.fields import CharField

from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from apps.models import İnstansiyaMahkemesiModel,instansiyaMahkemesihakimiModel,ikinciinstansiyaMahkemesihakimiModel



CHOOSEONE = (
    ('_____', '______'),
    ('1', '1'),
    ('1-1', '1-1'),
    ('7', '7'),
)

CHOOSETWO = (
    ('_____', '______'),
    ('Şikayət', 'Şikayət'),
    ('Protest', 'Protest'),
    ('Şikayət və protest', 'Şikayət və protest'),
)


CHOOSETREE = (
    ('_____', '______'),
    ('1 təmin edilmişdir', '1 təmin edilmişdir'),
    ('2 rədd edilmişdir', '2 rədd edilmişdir'),
    ('3 - baxılmamış saxlanılmışdır', '3 - baxılmamış saxlanılmışdır'),
)

CHOOSEFOUR = (
    ('_____', '______'),
    ('CPM 384-387-ci maddələrin tələbləri', 'CPM 384-387-ci maddələrin tələbləri'),
    ('CPM 385-388-ci maddələrin tələbləri', 'CPM 385-388-ci maddələrin tələbləri'),
    ('aidiyyət', 'aidiyyət'),
    ('apellyasiya şikayətinə xitam', 'apellyasiya şikayətinə xitam'),
    ('digər', 'digər'),
)

CHOOSEFIVE = (
    ('_____', '______'),
    ('Düzgün bəraət olunmadığına görə', 'Düzgün bəraət olunmadığına görə'),
    ('Cinayət tərkibi əməli və ittiham sübuta yetirilmədiyindən', 'Cinayət tərkibi əməli və ittiham sübuta yetirilmədiyindən'),
    ('Cinayət qanunu normasının düzgün tətbiq edilməməsi', 'Cinayət qanunu normasının düzgün tətbiq edilməməsi'),
    ('Digər əsaslar', 'Digər əsaslar'),
)



CHOOSESIX = (
    ('_____', '______'),
    ('Cəzanın ağırlaşdırılması', 'Cəzanın ağırlaşdırılması'),
    ('Cəzanın yüngülləşdirilməsi', 'Cəzanın yüngülləşdirilməsi'),
    ('Digər Əsaslar', 'Digər Əsaslar'),
)

CHOOSESEVEN = (
    ('_____', '______'),
    ('Dəyişdirilmədən saxlanılmışdır', 'Dəyişdirilmədən saxlanılmışdır'),
    ('Qərar ləğv edilmişdir', 'Qərar ləğv edilmişdir'),
    ('Qərar dəyişdirilmişdir', 'Qərar dəyişdirilmişdir'),
)
CHOOSEEIGHT = (
    ('_____', '______'),
    ('dövlət orqanının vəzifəli şəxsləri barəsində', 'dövlət orqanının vəzifəli şəxsləri barəsində'),
    ('müstəntiqlər, təhqiqatçılar və təhqiqat orqanının əməkdaşları', 'müstəntiqlər, təhqiqatçılar və təhqiqat orqanının əməkdaşları'),
    ('prokurorlar və ya prokurorluğun müstəntiqləri barəsində', 'prokurorlar və ya prokurorluğun müstəntiqləri barəsində'),
    ('birinci instansiya məhkəməsinin hakimləri barəsində', 'birinci instansiya məhkəməsinin hakimləri barəsində'),
)

CHOOSEFOUR = (
    ('_____', '______'),
    ('CPM 384-387-ci maddələrin tələbləri', 'CPM 384-387-ci maddələrin tələbləri'),
    ('CPM 385-388-ci maddələrin tələbləri', 'CPM 385-388-ci maddələrin tələbləri'),
    ('apellyasiya şikayətinə xitam', 'apellyasiya şikayətinə xitam'),
    ('digər', 'digər'),
)

class CinayetİsinNovları(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İsim')

    def __str__(self):
        return '%s %s' % (self.name, self.id)

    class Meta: 
        ordering = ['id']
        verbose_name = 'Cinayet İşin Növü'
        verbose_name_plural = 'Cinayet İşin Növları'

class Sikayətverilmisdir(models.Model):
    name                            = models.CharField(max_length=100,verbose_name='İsim')

    def __str__(self):
        return '%s %s' % (self.name, self.id)

    class Meta: 
        ordering = ['id']
        verbose_name = 'Şikayət verilmişdir'
        verbose_name_plural = 'Şikayət verilmişdir'


class Cinayet(models.Model):
    işin_nömrəsi                        = models.CharField(max_length=50000,blank=True,null=True)
    növ                                 = models.CharField(max_length=50, choices=CHOOSEONE, default='______')
    birinci_şəxs                        = models.BooleanField(blank=True,default=False)
    dahil_olmuşdur                      = models.DateField(blank=True,null=True,verbose_name='Daxil olmuşdur')
    isin_novu                           = models.ForeignKey(CinayetİsinNovları, verbose_name='Cinayətin növləri', related_name='cinayətin_növləri', on_delete=models.CASCADE,blank=False, null=True)
    instansiya_mahkemesi                = models.ForeignKey(İnstansiyaMahkemesiModel, related_name='cinayetmahkeme', on_delete=models.CASCADE,blank=False, null=True,verbose_name='1-ci instansiya məhkəməsi')
    instansiya_mahkemesi_hakimi         = models.ForeignKey(instansiyaMahkemesihakimiModel, related_name='cinayetmahkemehakimi', on_delete=models.CASCADE,blank=False, null=True,verbose_name='1-ci instansiya məhkəməsi hakimi')
    təqsirləndirilən_şəxs               = models.CharField(max_length=50000,blank=True, null=True) 
    Sikayət_verilmisdir                 = models.ForeignKey(Sikayətverilmisdir, related_name='sikayətverilmisdirmodel', on_delete=models.CASCADE,blank=False, null=True)
    Şikayət_Protest                     = models.CharField(max_length=50, choices=CHOOSETWO, default='______')
    iki_instansiya_mahkemesi_hakimi     = models.ForeignKey(ikinciinstansiyaMahkemesihakimiModel, related_name='cinayetmahkemehakimiiki', on_delete=models.CASCADE,blank=False, null=True,verbose_name='2-ci instansiya məhkəməsinin hakimi')
    etiraz                              = models.CharField(max_length=50, choices=CHOOSETREE, default='______')
    baxılmamışdır                       = models.CharField(max_length=50, choices=CHOOSEFOUR, default='______')
    hökm_dəyişdirilmədən_saxlanılmışdır = models.BooleanField(blank=True,default=False)
    hökm_ləğv_edilib_yeni_hökm_çıxarılıb        = models.CharField(max_length=5000, choices=CHOOSEFIVE, default='______')
    hökm_ləğv_edilib_icraata_xitam_verilib      = models.CharField(max_length=5000, choices=CHOOSEFIVE, default='______')
    hökm_ləğv_edilib_yeni_baxışa_göndərilib     = models.CharField(max_length=5000, choices=CHOOSEFIVE, default='______')
    qərar                                       = models.CharField(max_length=5000, choices=CHOOSESEVEN, default='______')
    hökm_dəyişdirilmişdir                       = models.CharField(max_length=5000, choices=CHOOSESIX, default='______')
    xüsusi_Qərar                                = models.CharField(max_length=5000, choices=CHOOSEEIGHT, default='______')
    dəftərxanaya_təhvil_verildi                 = models.DateField(blank=True,null=True)
    qeyd                                        = models.CharField(max_length=50000,blank=True, null=True)
    yoxlanıldı                                  = models.BooleanField(blank=True,default=False)            


    def get_export_queryset(self, request):
            return Cinayet.objects.filter(yoxlanıldı=True)

    def __str__(self):
        return '%s %s' % (self.növ, self.id)


    class Meta:
        ordering = ['id']
        verbose_name = 'Cinayət və Hərbi işlər'
        verbose_name_plural = 'Cinayət və Hərbi işləri'


