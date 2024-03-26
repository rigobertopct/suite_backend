from django.contrib import admin

from Espannol.boxeo.models import *


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria', 'peso_min', 'peso_max']


@admin.register(CodifResultado)
class CodifResultadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'resul', 'descripcion']


@admin.register(Golpe)
class GolpeAdmin(admin.ModelAdmin):
    list_display = ['id', 'golpe', 'siglas', 'efectivo']


admin.site.register(Pugil)
admin.site.register(Combate)
admin.site.register(Resultado)
admin.site.register(ContadorGolpes)
admin.site.register(ConfigGolpe)
