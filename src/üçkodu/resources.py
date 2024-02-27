from import_export import resources
from .models import ückodu

class ückoduResource(resources.ModelResource):

    def skip_row(self, instance, original):
        if instance.yoxlanıldı == True:
            return True
        else:
            return super(ückoduResource, self).skip_row(instance, original)

    class Meta:
        model = ückodu
        fields = ('id','işin_nömrəsi','növ','dahil_olmuşdur','instansiya_mahkemesi__name','instansiya_mahkemesi_hakimi_name','instansiya_məhkəməsinin_qərarının_tarixi','təqsirləndirilən_şəxs','məsuliyyətə_cəlb_olunmuş_şəxs','təqsirli_bilindiyi_maddə','qərarın_baxılma_nəticəsi','hakimin_qərarından','hakimin_qərarından','apellyasiya_məhkəməsinin_qərarı_ilə','iki_instansiya_mahkemesi_hakimi__name','dftərxanaya_verilmişdir','qeyd','yoxlanıldı')

