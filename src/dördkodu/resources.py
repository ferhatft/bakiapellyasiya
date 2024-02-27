from import_export import resources
from .models import döddkodu

class döddkoduResource(resources.ModelResource):

    def skip_row(self, instance, original):
        if instance.yoxlanıldı == True:
            return True
        else:
            return super(döddkoduResource, self).skip_row(instance, original)

    class Meta:
        model = döddkodu
        fields = ('id','işin_nömrəsi','növ','təqsirləndirilən_şəxs','cinayətin_növü__name','vəsatətlə_müraciət_edən_orqan__name','vəsatətin_mahiyyəti__name','instansiya_mahkemesi_hakimi_name','instansiya_məhkəməsinin_qərarının_tarixi','vəsatətin_baxılma_nəticəsi','qərarından__name','şikayət_protest','apellyasiya_məhkəməsində_baxılmışdır','iki_instansiya_mahkemesi_hakimi__name','dəftərxanaya_Verilmişdir','qeyd','yoxlanıldı',)



