from django.db import models
from django.db.models.fields import CharField

from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from apps.models import İnstansiyaMahkemesiModel,instansiyaMahkemesihakimiModel,ikinciinstansiyaMahkemesihakimiModel


CHOOSEONE = (
    ('_____', '______'),
    ('1.Cinayət', '1.Cinayət'),
    ('2.Hərbi', '2.Hərbi'),
    ('3.Mülki', '3.Mülki'),
    ('4.İqtisadi', '4.İqtisadi'),
    ('5.İnzibati', '5.İnzibati'),
    ('6.Digər', '6.Digər'),
)

CHOOSETWO = (
    ('_____', '______'),
    ('Ərizə', 'Ərizə'),
    ('şikayət', 'şikayət'),
    ('Təklif', 'Təklif'),
    ('FFE', 'FFE'),
)

CHOOSETREE = (
    ('_____', '______'),
    ('Poçt', 'Poçt'),
    ('Elektron poçt', 'Elektron poçt'),
    ('Vətəndaşdan', 'Vətəndaşdan'),
    ('Qaynar Xətt', 'Qaynar Xətt'),
    ('Faks', 'Faks'),
    ('Digər', 'Digər'),
    ('Teleqram', 'Teleqram'),
)


CHOOSEFOUR = (
    ('_____', '______'),
    ('AR Prezidentinin Adminstrasiyasından', 'AR Prezidentinin Adminstrasiyasından'),
    ('Milli Məclisdən', 'Milli Məclisdən'),
    ('Nazirlər Kabinetindən', 'Nazirlər Kabinetindən'),
    ('Ali Məhkəmədən', 'Ali Məhkəmədən'),
    ('Ərazi yurisdiksiyaya aid məhkəmələrdən', 'Ərazi yurisdiksiyaya aid məhkəmələrdən'),
)

CHOOSEFIVE = (
    ('_____', '______'),
    ('1-İşlərə obyektiv baxılmasına köməklik göstərilməsi barədə', '1-İşlərə obyektiv baxılmasına köməklik göstərilməsi barədə'),
    ('2-Məhkəmə sədrləri tərəfindən qəbul edilmələri barədə', '2-Məhkəmə sədrləri tərəfindən qəbul edilmələri barədə'),
    ('3-İşlə bağlı məlumat verilməsi', '3-İşlə bağlı məlumat verilməsi'),
    ('4-Məhkəmə aktları tələbi barədə', '4-Məhkəmə aktları tələbi barədə'),
    ('5-Vətəndaşların ehtimal olunan hüquqlarının pozulması barədə', '5-Vətəndaşların ehtimal olunan hüquqlarının pozulması barədə'),
    ('6-Məhkəmə Aktlarının icra olunmaması barədə', '6-Məhkəmə Aktlarının icra olunmaması barədə'),
    ('7-Məhkəmə Aktlarının birtərəfli qəbul edilməsi barədə', '7-Məhkəmə Aktlarının birtərəfli qəbul edilməsi barədə'),
    ('8-Məhkəmələrdə süründürməçiliyə yol verilməsi barədə', '8-Məhkəmələrdə süründürməçiliyə yol verilməsi barədə'),
    ('9-Hakimin qeyri qanuni hərəkətləri barədə', '9-Hakimin qeyri qanuni hərəkətləri barədə'),
    ('10-Vəkilin qeyri-qanuni hərəkətləri barədə', '10-Vəkilin qeyri-qanuni hərəkətləri barədə'),
    ('11-Digər', '11-Digər'),
    ('_____', '______'),
)

CHOOSESIX = (
    ('_____', '______'),
    ('Müsbət həll olunub', 'Müsbət həll olunub'),
    ('Qismən həll olunub', 'Qismən həll olunub'),
    ('Müvafiq izah verilib', 'Müvafiq izah verilib'),
    ('Əsassız sayılıb', 'Əsassız sayılıb'),
    ('İcradadır', 'İcradadır'),
    ('Müraciət aidiyyəti üzrə göndərilib', 'Müraciət aidiyyəti üzrə göndərilib'),
    ('Digər', 'Digər'),
)

CHOOSESEVEN = (
    ('_____', '______'),
    ('3 iş günü', '3 iş günü'),
    ('5 iş günü', '5 iş günü'),
    ('10 iş günü', '10 iş günü'),
    ('15 iş günü', '15 iş günü'),
    ('30 iş günü', '30 iş günü'),
    ('30 iş günündən artıq', '30 iş günündən artıq'),
)


class erizesikayet(models.Model):
    müraciətin_müəllifi                 = models.CharField(max_length=50000,blank=True,null=True)
    müraciətin_icraat_üzrə_növü         = models.CharField(max_length=500, choices=CHOOSEONE, default='______')
    digər_müraciətin_icraat_üzrə_növü                              = models.CharField(max_length=50000,blank=True,null=True)
    müraciət_daxil_olub                 = models.CharField(max_length=50000,blank=True,null=True)
    müraciətin_növü                     = models.CharField(max_length=500, choices=CHOOSETWO, default='______')
    daxil_olma_nömrə                    = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    daxil_olma_tarix                    = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    birbaşa                             = models.CharField(max_length=500, choices=CHOOSETREE, default='______')
    dövlət_orqanlarından_və_ya_digər_orqanlardan = models.CharField(max_length=500, choices=CHOOSEFOUR, default='______')
    digər_orqanlardan                   = models.CharField(max_length=50000,blank=True,null=True)   
    nəzarətdədir                        = models.BooleanField(blank=True,default=False)            
    hansı_müddət_müəyyən_edilib         = models.CharField(max_length=50000,blank=True,null=True)
    təkrar                              = models.BooleanField(blank=True,default=False)
    əvvəlki_nömrə_ve_Tarix              = models.CharField(max_length=50000,blank=True,null=True)
    daxil_olan_müraciətin_mövzuları     = models.CharField(max_length=500, choices=CHOOSEFIVE, default='______')
    digər_daxil_olan_müraciətin_mövzuları                               = models.CharField(max_length=50000,blank=True,null=True)   
    müraciətə_baxılmasının_nəticəsi     = models.CharField(max_length=500, choices=CHOOSESIX, default='______')
    digər_müraciətə_baxılmasının_nəticəsi                               = models.CharField(max_length=50000,blank=True,null=True)
    müraciətə_baxılma_müddəti           = models.CharField(max_length=500, choices=CHOOSESEVEN, default='______')
    qeyd                                = models.CharField(max_length=5000,blank=True, null=True) 
    yoxlanıldı                                  = models.BooleanField(blank=True,default=False)            


    def __str__(self):
        return '%s %s' % (self.müraciətin_müəllifi, self.id)


    class Meta:
        ordering = ['id']
        verbose_name = 'Ərizə Şikayət'
        verbose_name_plural = 'Ərizə Şikayət'

