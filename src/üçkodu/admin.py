from django.contrib import admin
from .models import ückodu
# Register your models here
# 
# 
from .resources import ückoduResource
from advanced_filters.admin import AdminAdvancedFiltersMixin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(ückodu)


class ückoduAdmin(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    
    # readonly_fields = ('rating','created_date')

    list_display = ('işin_nömrəsi', 'növ','dahil_olmuşdur','instansiya_mahkemesi','instansiya_mahkemesi_hakimi', 'instansiya_məhkəməsinin_qərarının_tarixi','təqsirləndirilən_şəxs', )

    # list_filter = ('name', 'author', 'author_email','imported', 'published','price', 'categories',)

    # ordering = ('-name',)
    
    advanced_filter_fields = (
        'işin_nömrəsi', 'növ','dahil_olmuşdur', ('instansiya_mahkemesi__name', 'instansiya mahkemesi'), ('instansiya_mahkemesi_hakimi__name', 'instansiya mahkemesi hakimi'), 'instansiya_məhkəməsinin_qərarının_tarixi','təqsirləndirilən_şəxs', 'məsuliyyətə_cəlb_olunmuş_şəxs','təqsirli_bilindiyi_maddə','qərarın_baxılma_nəticəsi','hakimin_qərarından','apellyasiya_məhkəməsinin_qərarı_ilə', ('iki_instansiya_mahkemesi_hakimi__name', 'iki instansiya mahkemesi hakimi'),'dftərxanaya_verilmişdir','qeyd',
    )
    resource_class = ückoduResource

admin.site.register(ückodu, ückoduAdmin)
