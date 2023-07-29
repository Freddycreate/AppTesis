#from daterange_filter.filter import DateRangeFilter
from django.contrib import admin
from import_export import resources

# Importar las clases del modelo
from molienda.models import Atomizado, Barbotina, Granulometria, Planta
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class AtomizadoResource(resources.ModelResource):
    class Meta:
        model = Atomizado
        exclude = ('usuario',)


class AtomizadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resources_class = AtomizadoResource
    list_display = ('id', 'planta', 'fecha', 'hora', 'codigo', 'nroSilo', 'humedad', 'observaciones', 'usuario',)
    search_fields = ('fecha', 'codigo', 'nroSilo',)
    filter = ('fecha', 'nroSilo', 'usuario',)


admin.site.register(Atomizado, AtomizadoAdmin)


class BarbotinaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora', 'densidad', 'viscosidad', 'residuo', 'planta', 'usuario',)
    search_fields = ('planta', 'usuario', 'fecha', 'codigo',)


admin.site.register(Barbotina, BarbotinaAdmin)


class GranulometriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'fecha', 'hora', 'malla500', 'malla425', 'malla300', 'malla180', 'fondo', 'planta', 'usuario',)
    search_fields = ('planta', 'usuario', 'fecha', 'codigo',)


admin.site.register(Granulometria, GranulometriaAdmin)


admin.site.register(Planta)

