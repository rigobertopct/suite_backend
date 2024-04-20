from django.contrib import admin

from Deportes.models import *


# Register your models here.

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'codigo']


@admin.register(Deporte)
class DeporteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'siglas']
