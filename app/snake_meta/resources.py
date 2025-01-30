from import_export import resources
from import_export.exceptions import ImportExportError
from .models import Serpiente

class SerpienteResource(resources.ModelResource):
    class Meta:
        model = Serpiente
        import_id_fields = ('idSerpiente',)

