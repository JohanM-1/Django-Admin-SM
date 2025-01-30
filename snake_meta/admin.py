from django.contrib import admin

from snake_meta.resources import SerpienteResource
from .models import Serpiente, Reporte, Usuario
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Serpiente)
class SerpienteAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_classes = [SerpienteResource]
    list_display = ['nombre3', 'nombreCientifico', 'especie', 'familia', 'venenosa']
    list_filter = ['venenosa', 'familia', 'genero']
    search_fields = ['nombre3', 'nombreCientifico', 'descripcion']
    list_per_page = 20


@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario_id_usuario', 'serpientes_id_serpientes', 'created_at', 'descripcion'  ]
    list_filter = ['usuario_id_usuario', 'serpientes_id_serpientes', 'created_at']
    search_fields = ['usuario_id_usuario', 'serpientes_id_serpientes', 'comentario']
    list_per_page = 20

@admin.register(Usuario)
class UsuarioAdmin(ImportExportModelAdmin):
    list_display = ['nombre', 'apellido', 'correo', 'contraseña']
    search_fields = ['nombre', 'apellido', 'correo']
    list_per_page = 20

