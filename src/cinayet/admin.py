from django.contrib import admin
from .models import Cinayet,CinayetİsinNovları,Sikayətverilmisdir
# Register your models here.
admin.site.register(CinayetİsinNovları)
admin.site.register(Sikayətverilmisdir)



from django.contrib import admin
from .resources import CinayetResource

from .models import Cinayet
from advanced_filters.admin import AdminAdvancedFiltersMixin
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class CinayetAdmin(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    
    # readonly_fields = ('rating','created_date')

    # list_display = ('name', 'author', 'author_email','imported', 'published','price')

    # list_filter = ('name', 'author', 'author_email','imported', 'published','price', 'categories',)

    # ordering = ('-name',)
    
    list_display = ( 'işin_nömrəsi','növ','birinci_şəxs','dahil_olmuşdur','isin_novu','instansiya_mahkemesi','instansiya_mahkemesi_hakimi','Şikayət_Protest','iki_instansiya_mahkemesi_hakimi','etiraz','baxılmamışdır','hökm_dəyişdirilmədən_saxlanılmışdır','hökm_ləğv_edilib_yeni_hökm_çıxarılıb','hökm_ləğv_edilib_icraata_xitam_verilib', 'hökm_ləğv_edilib_yeni_baxışa_göndərilib','qərar','hökm_dəyişdirilmişdir','dəftərxanaya_təhvil_verildi',)

    advanced_filter_fields = ( 'işin_nömrəsi','növ', 'birinci_şəxs','dahil_olmuşdur', ('isin_novu__name', 'isin novu') , ('instansiya_mahkemesi__name', 'instansiya mahkemesi'), ('instansiya_mahkemesi_hakimi__name', 'instansiya mahkemesi hakimi'), 'Şikayət_Protest',('iki_instansiya_mahkemesi_hakimi__name', 'iki instansiya mahkemesi hakimi'),'etiraz','baxılmamışdır','hökm_dəyişdirilmədən_saxlanılmışdır','hökm_ləğv_edilib_yeni_hökm_çıxarılıb','hökm_ləğv_edilib_icraata_xitam_verilib','hökm_ləğv_edilib_yeni_baxışa_göndərilib','qərar', 'hökm_dəyişdirilmişdir','xüsusi_Qərar','dəftərxanaya_təhvil_verildi','qeyd',
    )
    resource_class = CinayetResource

    
    def get_export_queryset(self, request):
            return Cinayet.objects.filter(yoxlanıldı=True)

    # def get_import_queryset(self, request):
    #         return Cinayet.objects.filter(yoxlanıldı=False)
admin.site.register(Cinayet, CinayetAdmin)

