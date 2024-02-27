from import_export import resources
from .models import Cinayet

class CinayetResource(resources.ModelResource):
    
    def skip_row(self, instance, original):
        if instance.yoxlanıldı == True:
            return True
        else:
            return super(CinayetResource, self).skip_row(instance, original)

    class Meta:
        model = Cinayet
        fields = ('id','işin_nömrəsi','növ','birinci_şəxs','dahil_olmuşdur','isin_novu__name','instansiya_mahkemesi__name','instansiya_mahkemesi_hakimi__name','təqsirləndirilən_şəxs','Sikayət_verilmisdir__name','Şikayət_Protest','iki_instansiya_mahkemesi_hakimi__name','etiraz','baxılmamışdır','hökm_dəyişdirilmədən_saxlanılmışdır','hökm_ləğv_edilib_yeni_hökm_çıxarılıb','hökm_ləğv_edilib_icraata_xitam_verilib','hökm_ləğv_edilib_yeni_baxışa_göndərilib','qərar','hökm_dəyişdirilmişdir','xüsusi_Qərar','dəftərxanaya_təhvil_verildi','qeyd','yoxlanıldı')
