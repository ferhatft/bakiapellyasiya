from django.contrib import admin
from .models import erizesikayet
from .resources import erizesikayetResource

from advanced_filters.admin import AdminAdvancedFiltersMixin
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class erizesikayetAdmin(AdminAdvancedFiltersMixin,ImportExportModelAdmin):
    
    # readonly_fields = ('rating','created_date')

    # list_display = ('name', 'author', 'author_email','imported', 'published','price')

    # list_filter = ('name', 'author', 'author_email','imported', 'published','price', 'categories',)

    # ordering = ('-name',)
    
    advanced_filter_fields = (
        'müraciətin_müəllifi','müraciətin_icraat_üzrə_növü','müraciət_daxil_olub','müraciətin_növü','daxil_olma_tarix','daxil_olma_nömrə','birbaşa','dövlət_orqanlarından_və_ya_digər_orqanlardan','digər_orqanlardan','nəzarətdədir','hansı_müddət_müəyyən_edilib','təkrar','əvvəlki_nömrə_ve_Tarix','daxil_olan_müraciətin_mövzuları','müraciətə_baxılmasının_nəticəsi','müraciətə_baxılma_müddəti','qeyd'
    )
    resource_class = erizesikayetResource

admin.site.register(erizesikayet, erizesikayetAdmin)
