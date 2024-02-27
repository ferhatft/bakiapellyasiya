from import_export import resources
from .models import inziqmul

class inziqmulResource(resources.ModelResource):

    def skip_row(self, instance, original):
        if instance.yoxlanıldı == True:
            return True
        else:
            return super(inziqmulResource, self).skip_row(instance, original)

    class Meta:
        model = inziqmul
        fields = ('id','işin_nömrəsi','növ','daxil_olduğu_tarix','apellyasiya_sikayati_verilmişdir','qısa_qeyd','instansiyaya_daxil_olmuşdur','instansiya_mahkemesi__name','instansiya_mahkemesi_hakimi__name','iddiaçı','cavabdeh','iddianın_mahiyyəti','hakimə_edilmiş_etiraz','qeyri_mümkün_hesab_edilərək_icraata_xitam_verilmişdir','aidiyyət','isin_novu__name','apellyasiya_qaydasında_baxılmışdır','icraat_dayandırılmışdır','nəticə__name','yekun_qərar','iki_instansiya_mahkemesi_hakimi__name','xüsusi_Qərar','dövlət_rüsumu','dəftərxanaya_təhvil_verildi','qeyd','yoxlanıldı')





