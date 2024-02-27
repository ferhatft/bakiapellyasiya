from django.contrib import admin

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .models import İnstansiyaMahkemesiModel,instansiyaMahkemesihakimiModel,ikinciinstansiyaMahkemesihakimiModel
from advanced_filters.admin import AdminAdvancedFiltersMixin
from import_export.admin import ImportExportModelAdmin
# Register your models here.



# class MulkiAdmin(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    
#     # readonly_fields = ('rating','created_date')

#     # list_display = ('name', 'author', 'author_email','imported', 'published','price')

#     # list_filter = ('name', 'author', 'author_email','imported', 'published','price', 'categories',)

#     # ordering = ('-name',)
    
#     advanced_filter_fields = (
#         'isin_nömresi', 'dahil_olmuşdur','apellyasiya_sikayati_verilmişdir','qısa_qeyd', ('instansiya_mahkemesi__name', 'instansiya mahkemesi'), ('instansiya_mahkemesi_hakimi__name', 'instansiya mahkemesi hakimi'),'iddiaçı','cavabdeh','iddianın_maliyeti','hakima_edilmiş_etiraz','qeyri_mümkün_hesab_edilerek_icraata_xitam_verilmişdir','aidiyyat',('isin_novu__name', 'isin novu') ,'apellyasiya_qaydasında_bakılmısdır',('netica__name', 'netica'),'yekun_qarar', ('iki_instansiya_mahkemesi_hakimi__name', 'iki instansiya mahkemesi hakimi'),'xüsusi_wawrardad','dövlat_rüsumu','qısa_qeyd','deftarxanaya_tahvil_verildi','qeyd'  
#     )
#     resource_class = MulkiResource

# admin.site.register(Mülki, MulkiAdmin)


admin.site.register(ikinciinstansiyaMahkemesihakimiModel)
admin.site.register(instansiyaMahkemesihakimiModel)
admin.site.register(İnstansiyaMahkemesiModel)


admin.site.site_header = 'BAKI APELLYASİYA MƏHKƏMƏSİ'