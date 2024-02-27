from import_export import resources
from .models import erizesikayet

class erizesikayetResource(resources.ModelResource):

    def skip_row(self, instance, original):
        if instance.yoxlanıldı == True:
            return True
        else:
            return super(erizesikayetResource, self).skip_row(instance, original)

    class Meta:
        model = erizesikayet


