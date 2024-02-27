from django.contrib import admin
from .models import inziqmul,inziqmulisinNovları,inziqmulnəticə

from .resources import  inziqmulResource
from advanced_filters.admin import AdminAdvancedFiltersMixin
from import_export.admin import ImportExportModelAdmin

admin.site.register(inziqmulisinNovları)
admin.site.register(inziqmulnəticə)




class inziqmulAdmin(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    
    # readonly_fields = ('rating','created_date')

    # list_display = ('name', 'author', 'author_email','imported', 'published','price')

    # list_filter = ('name', 'author', 'author_email','imported', 'published','price', 'categories',)

    # ordering = ('-name',)
    
    advanced_filter_fields = (
        'işin_nömrəsi', 'növ','daxil_olduğu_tarix', 'apellyasiya_sikayati_verilmişdir','qısa_qeyd','instansiyaya_daxil_olmuşdur', ('instansiya_mahkemesi__name', 'instansiya mahkemesi'), ('instansiya_mahkemesi_hakimi__name', 'instansiya mahkemesi hakimi'), 'iddiaçı','cavabdeh','iddianın_mahiyyəti','hakimə_edilmiş_etiraz', 'qeyri_mümkün_hesab_edilərək_icraata_xitam_verilmişdir','aidiyyət', ('isin_novu__name', 'isin novu'), 'apellyasiya_qaydasında_baxılmışdır','icraat_dayandırılmışdır', ('nəticə__name', 'nəticə'), 'yekun_qərar',('iki_instansiya_mahkemesi_hakimi__name', 'iki instansiya mahkemesi hakimi'),'xüsusi_Qərar','dövlət_rüsumu','dəftərxanaya_təhvil_verildi','qeyd',
    )
    resource_class = inziqmulResource

admin.site.register(inziqmul, inziqmulAdmin)
