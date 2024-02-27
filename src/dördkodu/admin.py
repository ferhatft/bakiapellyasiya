from django.contrib import admin
from.models import döddkodu,CinayetNovları,Vəsatətlə_müraciət_edən_orqan,Vəsatətin_Mahiyyəti

from .resources import döddkoduResource
from advanced_filters.admin import AdminAdvancedFiltersMixin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(CinayetNovları)
admin.site.register(Vəsatətlə_müraciət_edən_orqan)
admin.site.register(Vəsatətin_Mahiyyəti)


# Register your models here.



class döddkoduAdmin(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    
    # readonly_fields = ('rating','created_date')

    # list_display = ('name', 'author', 'author_email','imported', 'published','price')

    # list_filter = ('name', 'author', 'author_email','imported', 'published','price', 'categories',)

    # ordering = ('-name',)
    
    advanced_filter_fields = (
        'işin_nömrəsi', 'növ','təqsirləndirilən_şəxs', ('cinayətin_növü__name', 'cinayətin növü'), ('vəsatətlə_müraciət_edən_orqan__name', 'vəsatətlə müraciət edən orqan'), ('vəsatətin_mahiyyəti__name', 'vəsatətin mahiyyəti'), ('instansiya_mahkemesi_hakimi__name', 'instansiya mahkemesi hakimi'), 'instansiya_məhkəməsinin_qərarının_tarixi','vəsatətin_baxılma_nəticəsi', ('qərarından__name', 'qərarından'), 'şikayət_protest', 'apellyasiya_məhkəməsində_baxılmışdır', ('iki_instansiya_mahkemesi_hakimi__name', 'iki instansiya mahkemesi hakimi'),'dəftərxanaya_Verilmişdir','qeyd',
    )
    resource_class = döddkoduResource

admin.site.register(döddkodu, döddkoduAdmin)
