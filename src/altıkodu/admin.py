from django.contrib import admin
from.models import altıkodu
from .resources import altıkoduResource
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class altıkoduAdmin(ImportExportModelAdmin):
    list_display = ('işin_nömrəsi','yoxlanıldı','növ','daxil_olduğu_tarix','şikayətlə_müraciət_edən_şəxs','şikayətlə_müraciət_edən_şəxs','şikayət_verilmişdir','bir_instansiya_məhkəməsində_baxılmışdır','instansiya_mahkemesi','instansiya_mahkemesi_hakimi','şikayətə_baxılmanın_nəticəsi','apellyasiya_qayadısnda','apellyasiya_məhkəməsində_baxılmışdır','iki_instansiya_mahkemesi_hakimi','apellyasiya_məhkəməsi','iş_dəftərxanaya_təhvil_verilmişdir',)
    list_editable = ('yoxlanıldı',)
    
    resource_class = altıkoduResource

admin.site.register(altıkodu, altıkoduAdmin)

