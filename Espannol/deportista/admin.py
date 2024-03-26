from django.contrib import admin

from Espannol.deportista.models import Deportista, DeportistaDisciplina


# Register your models here.


@admin.register(Deportista)
class DeportistaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'edad', 'codigo']


@admin.register(DeportistaDisciplina)
class DeportistaDisciplinaAdmin(admin.ModelAdmin):
    list_display = ['deportista', 'disciplina']
