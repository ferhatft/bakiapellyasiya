from import_export import resources
from .models import altıkodu

class altıkoduResource(resources.ModelResource):

    class Meta:
        model = altıkodu
        fields = ('id','işin_nömrəsi','növ','daxil_olduğu_tarix','şikayətlə_müraciət_edən_şəxs','şikayət_verilmişdir','bir_instansiya_məhkəməsində_baxılmışdır','instansiya_mahkemesi__name','instansiya_mahkemesi_hakimi_name','şikayətə_baxılmanın_nəticəsi','apellyasiya_qayadısnda','apellyasiya_məhkəməsində_baxılmışdır','şikayət_protest','apellyasiya_məhkəməsində_baxılmışdır','iki_instansiya_mahkemesi_hakimi__name','apellyasiya_məhkəməsi','iş_dəftərxanaya_təhvil_verilmişdir','qeyd','yoxlanıldı',)



